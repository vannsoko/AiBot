from context.summary.handbook import handbook_summary
from context.summary.status import status_summary


ai_summary: dict[str, str] = {
    "handbook": handbook_summary,
    "statute": status_summary,
}
