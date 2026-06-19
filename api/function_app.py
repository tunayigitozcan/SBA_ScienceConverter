"""Azure Functions V2 backend for the Science Converter.

Single HTTP endpoint `/api/convert` that accepts JSON:
    { "kind": "<conversion key>", "value": <number> }
and returns:
    { "result": <number> }

The math is the same as converter.py in the repo root so the v1 in-browser
results and the v2 server-side results stay identical.
"""
import json
import azure.functions as func

KM_PER_MILE = 1.609344
LB_PER_KG = 2.20462

CONVERTERS = {
    "km_to_miles": lambda v: v / KM_PER_MILE,
    "miles_to_km": lambda v: v * KM_PER_MILE,
    "c_to_f":      lambda v: v * 9 / 5 + 32,
    "f_to_c":      lambda v: (v - 32) * 5 / 9,
    "kg_to_lb":    lambda v: v * LB_PER_KG,
    "lb_to_kg":    lambda v: v / LB_PER_KG,
}

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)


def _json(status: int, payload: dict) -> func.HttpResponse:
    return func.HttpResponse(
        body=json.dumps(payload),
        status_code=status,
        mimetype="application/json",
    )


@app.route(route="convert", methods=["POST", "OPTIONS"])
def convert(req: func.HttpRequest) -> func.HttpResponse:
    if req.method == "OPTIONS":
        return func.HttpResponse(status_code=204)

    try:
        body = req.get_json()
    except ValueError:
        return _json(400, {"error": "Request body must be JSON"})

    kind = body.get("kind")
    raw_value = body.get("value")

    if kind not in CONVERTERS:
        return _json(400, {"error": f"Unknown conversion kind: {kind}"})

    try:
        value = float(raw_value)
    except (TypeError, ValueError):
        return _json(400, {"error": "Field 'value' must be a number"})

    result = CONVERTERS[kind](value)
    return _json(200, {"kind": kind, "input": value, "result": result})


@app.route(route="health", methods=["GET"])
def health(_: func.HttpRequest) -> func.HttpResponse:
    return _json(200, {"status": "ok"})
