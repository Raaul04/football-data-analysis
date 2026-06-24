from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt


def main():
    output_dir = Path("outputs")
    output_dir.mkdir(exist_ok=True)

    players = pd.read_csv("data/players.csv", skipinitialspace=True)

    players.columns = players.columns.str.strip()

    for column in players.select_dtypes(include="object").columns:
        players[column] = players[column].str.strip()

    print("=== Football Data Analysis ===")
    print()

    print("Dataset:")
    print(players)
    print()

    # Calculate total goal contributions
    players["goal_contributions"] = players["goals"] + players["assists"]

    # Calculate goal contributions per 90 minutes
    players["goal_contributions_per_90"] = (
        players["goal_contributions"] / players["minutes"] * 90
    ).round(2)

    top_players = players.sort_values(by="goal_contributions", ascending=False)

    print("Top players by goal contributions:")
    print(top_players[["name", "team", "goals", "assists", "goal_contributions"]])
    print()

    top_players.to_csv(output_dir / "top_players.csv", index=False)
    print("Top players saved as outputs/top_players.csv")
    print()

    top_players_per_90 = players.sort_values(
        by="goal_contributions_per_90",
        ascending=False
    )

    print("Top players by goal contributions per 90 minutes:")
    print(
        top_players_per_90[
            ["name", "team", "minutes", "goal_contributions", "goal_contributions_per_90"]
        ]
    )
    print()

    top_players_per_90.to_csv(output_dir / "top_players_per_90.csv", index=False)
    print("Top players saved as outputs/top_players_per_90.csv")
    print()

    average_goals_by_position = players.groupby("position")["goals"].mean()

    print("Average goals by position:")
    print(average_goals_by_position)
    print()

    team_summary = players.groupby("team")[["goals", "assists", "goal_contributions"]].sum()
    team_summary = team_summary.sort_values(by="goal_contributions", ascending=False)

    print("Team summary:")
    print(team_summary)
    print()

    team_summary.to_csv(output_dir / "team_summary.csv")
    print("Team summary saved as outputs/team_summary.csv")
    print()

    top_15_players = top_players.head(15)

    # First chart: total goal contributions
    plt.figure(figsize=(10, 6))
    plt.barh(top_15_players["name"], top_15_players["goal_contributions"])
    plt.title("Top 15 Players by Goal Contributions")
    plt.xlabel("Goals + Assists")
    plt.ylabel("Player")
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.savefig(output_dir / "goal_contributions.png")
    plt.close()

    print("Chart saved as outputs/goal_contributions.png")

    top_15_players_per_90 = top_players_per_90.head(15)

    # Second chart: goal contributions per 90 minutes
    plt.figure(figsize=(10, 6))
    plt.barh(
        top_15_players_per_90["name"],
        top_15_players_per_90["goal_contributions_per_90"]
    )
    plt.title("Top 15 Players by Goal Contributions per 90 Minutes")
    plt.xlabel("Goal Contributions per 90")
    plt.ylabel("Player")
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.savefig(output_dir / "goal_contributions_per_90.png")
    plt.close()

    print("Chart saved as outputs/goal_contributions_per_90.png")


if __name__ == "__main__":
    main()