import pandas as pd
import matplotlib.pyplot as plt


def main():
    players = pd.read_csv("data/players.csv")

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
    )

    top_players = players.sort_values(by="goal_contributions", ascending=False)

    print("Top players by goal contributions:")
    print(top_players[["name", "team", "goals", "assists", "goal_contributions"]])
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

    average_goals_by_position = players.groupby("position")["goals"].mean()

    print("Average goals by position:")
    print(average_goals_by_position)
    print()

    team_summary = players.groupby("team")[["goals", "assists", "goal_contributions"]].sum()
    team_summary = team_summary.sort_values(by="goal_contributions", ascending=False)

    print("Team summary:")
    print(team_summary)
    print()

    # First chart: total goal contributions
    plt.figure(figsize=(10, 6))
    plt.bar(top_players["name"], top_players["goal_contributions"])
    plt.title("Goal Contributions by Player")
    plt.xlabel("Player")
    plt.ylabel("Goals + Assists")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig("goal_contributions.png")

    print("Chart saved as goal_contributions.png")

    # Second chart: goal contributions per 90 minutes
    plt.figure(figsize=(10, 6))
    plt.bar(top_players_per_90["name"], top_players_per_90["goal_contributions_per_90"])
    plt.title("Goal Contributions per 90 Minutes")
    plt.xlabel("Player")
    plt.ylabel("Goal Contributions per 90")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig("goal_contributions_per_90.png")

    print("Chart saved as goal_contributions_per_90.png")


if __name__ == "__main__":
    main()