# TVMaze search API: JSON structure

Request: `GET https://api.tvmaze.com/search/shows?q=<search term>`

The response is a **list**. Each item is one search match, and each match has two keys:

```json
[
  {
    "score": 0.9,
    "show": { "name": "Sherlock", "genres": ["Drama", "Crime", "Mystery"], "rating": { "average": 8.9 }, "...": "..." }
  }
]
```

- **`score`**: how closely the show matches the search term.
- **`show`**: the details of the show. The script reads everything from here.

## Fields the script uses

| What it is | Where it is in the JSON | Python access | Notes |
|---|---|---|---|
| Show name | `show.name` | `result["show"]["name"]` | Always present. |
| Genre | `show.genres` | `result["show"]["genres"]` | A list of strings. It can be empty, so the script shows "Unknown". |
| Rating | `show.rating.average` | `result["show"]["rating"]["average"]` | A number, or `null` when there is no rating. The script shows "No rating". |

## Other fields in `show` (not used)

`id`, `url`, `type`, `language`, `status`, `runtime`, `premiered`, `ended`, `network`, `image`, `summary` (HTML text), `externals`, `updated`, `_links`, and more.

## Converting to Python objects

The script copies the fields it needs into a `Show` dataclass (`parse_show` in `tvmaze_search.py`). The rest of the script then works with `show.name`, `show.genres` and `show.rating` rather than nested dictionary lookups.
