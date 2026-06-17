import pandas as pd
import matplotlib.pyplot as plt


def main():
    players = pd.read_csv("data/players.csv")

    print("=== Football Data Analysis ===")
    print()

    print("Dataset:")
    print(players)
    print()

    players["goal_contributions"] = players["goals"] + players["assists"]

    top_players = players.sort_values(by="goal_contributions", ascending=False)

    print("Top players by goal contributions:")
    print(top_players[["name", "team", "goals", "assists", "goal_contributions"]])
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

    plt.figure(figsize=(10, 6))
    plt.bar(top_players["name"], top_players["goal_contributions"])
    plt.title("Goal Contributions by Player")
    plt.xlabel("Player")
    plt.ylabel("Goals + Assists")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()

    plt.savefig("goal_contributions.png")

    print("Chart saved as goal_contributions.png")


if __name__ == "__main__":
    main()