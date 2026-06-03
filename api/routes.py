from fastapi import APIRouter

from services.search_service import multi_search
from services.identity_service import compute_identity
from services.parser_service import extract_platforms, extract_hashtags
from services.metrics_service import compute_metrics
from services.summary_service import generate_summary

router = APIRouter()

@router.get("/intelligence")
def intelligence(name: str):

    results = multi_search(name)

    profiles = compute_identity(name, results)

    categorized = extract_platforms(profiles)

    hashtags = extract_hashtags([r["title"] for r in results])

    metrics = compute_metrics(profiles, len(results), categorized)

    return {
        "input": name,
        **categorized,
        "hashtags": hashtags,
        "metrics": metrics,

        "summary": generate_summary({
            **categorized,
            "metrics": metrics
        })
    }