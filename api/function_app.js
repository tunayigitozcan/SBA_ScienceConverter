// Azure Functions V2 (Node.js) — Science Converter backend.
// Same JSON contract as the Python version it replaces:
//   POST /api/convert  { "kind": "<key>", "value": <number> } -> { "result": <number> }
// Switched from Python to Node.js because Azure for Students does not currently
// expose the Linux + Python + Consumption combination in any region.

const { app } = require("@azure/functions");

const KM_PER_MILE = 1.609344;
const LB_PER_KG = 2.20462;

const CONVERTERS = {
  km_to_miles: (v) => v / KM_PER_MILE,
  miles_to_km: (v) => v * KM_PER_MILE,
  c_to_f:      (v) => (v * 9) / 5 + 32,
  f_to_c:      (v) => ((v - 32) * 5) / 9,
  kg_to_lb:    (v) => v * LB_PER_KG,
  lb_to_kg:    (v) => v / LB_PER_KG,
};

app.http("convert", {
  methods: ["POST", "OPTIONS"],
  authLevel: "anonymous",
  handler: async (request) => {
    if (request.method === "OPTIONS") {
      return { status: 204 };
    }

    let body;
    try {
      body = await request.json();
    } catch {
      return { status: 400, jsonBody: { error: "Request body must be JSON" } };
    }

    const { kind, value } = body || {};

    if (!CONVERTERS[kind]) {
      return { status: 400, jsonBody: { error: `Unknown conversion kind: ${kind}` } };
    }

    const numeric = Number(value);
    if (!Number.isFinite(numeric)) {
      return { status: 400, jsonBody: { error: "Field 'value' must be a number" } };
    }

    const result = CONVERTERS[kind](numeric);
    return { jsonBody: { kind, input: numeric, result } };
  },
});

app.http("health", {
  methods: ["GET"],
  authLevel: "anonymous",
  handler: async () => ({ jsonBody: { status: "ok" } }),
});
