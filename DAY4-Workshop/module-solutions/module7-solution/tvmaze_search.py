import json
import logging
import requests

logging.basicConfig(
    filename="automation.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def load_config(config_file):
    """Load configuration settings."""
    with open(config_file) as file:
        return json.load(file)


def get_tv_shows(search_term):
    """Retrieve TV show information from the TVMaze API."""
    logging.info("Searching for '%s'", search_term)
    url = f"https://api.tvmaze.com/search/shows?q={search_term}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def save_report(results, minimum_rating, report_file):
    """Save matching shows to a report file."""
    with open(report_file, "w") as file:
        file.write("TV Show Report\n")
        file.write("=" * 40 + "\n\n")

        count = 0
        for result in results:
            show = result["show"]
            rating = show["rating"]["average"]

            if rating is not None and rating >= minimum_rating:
                genres = ", ".join(show["genres"])
                file.write(f"Name   : {show['name']}\n")
                file.write(f"Genres : {genres}\n")
                file.write(f"Rating : {rating}\n")
                file.write("-" * 40 + "\n")
                count += 1

    logging.info("%s shows written to report.", count)


def main():
    logging.info("Automation started.")
    config = load_config("config.json")
    results = get_tv_shows(config["search_term"])
    save_report(
        results,
        config["minimum_rating"],
        "tv_report.txt"
    )
    logging.info("Automation completed successfully.")


if __name__ == "__main__":
    main()
