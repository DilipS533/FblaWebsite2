export default function handler(req, res) {
  return res.status(200).json({
    hasKey: !!process.env.OPENAI_API_KEY,
    keyLength: process.env.OPENAI_API_KEY ? process.env.OPENAI_API_KEY.length : 0,
    startsWithSk: process.env.OPENAI_API_KEY ? process.env.OPENAI_API_KEY.startsWith("sk-") : false,
    vercelEnv: process.env.VERCEL_ENV || "unknown"
  });
}