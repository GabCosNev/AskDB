import json
from app.config import DATA_SOURCE, DATA_PATH, DATABASE_URL


def _search_json(event_type: str | None, limit: int) -> list[dict]:
    with DATA_PATH.open("r", encoding="utf-8") as file:
        events = json.load(file)

    result = [
        {
            "id": e["id"],
            "title": e["title"],
            "content": e["content"],
            "event_type": e["eventType"],
            "start_date": e["startDate"],
            "end_date": e["endDate"],
        }
        for e in events
        if e.get("status") == "APPROVED"
        and (event_type is None or e.get("eventType") == event_type)
    ]
    result.sort(key=lambda e: e["start_date"], reverse=True)
    return result[:limit]


def _search_db(event_type: str | None, limit: int) -> list[dict]:
    import psycopg
    from psycopg.rows import dict_row

    conditions = ["status = 'APPROVED'"]
    params: dict = {"limit": limit}
    if event_type:
        conditions.append('"eventType" = %(event_type)s::"EventType"')
        params["event_type"] = event_type

    sql = f"""
        SELECT id, title, content,
               "eventType" AS event_type,
               "startDate" AS start_date,
               "endDate" AS end_date
        FROM "Post"
        WHERE {' AND '.join(conditions)}
        ORDER BY "startDate" DESC
        LIMIT %(limit)s
    """
    with psycopg.connect(DATABASE_URL, row_factory=dict_row) as conn:
        return conn.execute(sql, params).fetchall()


def search_approved_posts(event_type: str | None, limit: int = 50) -> list[dict]:
    if DATA_SOURCE == "db":
        return _search_db(event_type, limit)
    return _search_json(event_type, limit)