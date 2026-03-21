export default async function handler(req, res) {
  // Only allow POST requests
  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method naturally not allowed' });
  }

  try {
    const data = req.body;

    // AIRTABLE SETUP (CRM)
    const AIRTABLE_API_KEY = process.env.AIRTABLE_API_KEY;
    const AIRTABLE_BASE_ID = process.env.AIRTABLE_BASE_ID;
    // Set 'Table 1' as your default table name in Airtable
    const AIRTABLE_TABLE_NAME = process.env.AIRTABLE_TABLE_NAME || 'Table 1';

    if (!AIRTABLE_API_KEY || !AIRTABLE_BASE_ID) {
      console.warn("CRM Credentials missing. Logging lead locally:", data);
      // Fallback for when env variables aren't set yet
      return res.status(200).json({ success: true, message: 'Simulated submission' });
    }

    const response = await fetch(`https://api.airtable.com/v0/${AIRTABLE_BASE_ID}/${AIRTABLE_TABLE_NAME}`, {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${AIRTABLE_API_KEY}`,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        typecast: true,
        records: [
          {
            fields: {
              "Company Name": data.companyName || "Unknown",
              "Email": data.email || "Unknown",
              "Debt Amount": Number(data.debtAmount) || 0,
              "Message": data.message || ""
            }
          }
        ]
      })
    });

    if (!response.ok) {
      const errorData = await response.json();
      console.error("Airtable Error:", errorData);
      return res.status(400).json({ error: JSON.stringify(errorData) });
    }

    // Success
    return res.status(200).json({ success: true, message: 'Lead added to CRM' });

  } catch (error) {
    console.error('Submission Error:', error);
    return res.status(500).json({ error: error.message || 'Failed to process lead submission' });
  }
}
