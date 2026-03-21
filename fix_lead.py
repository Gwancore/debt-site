with open("api/submit-lead.js", "r", encoding="utf-8") as f:
    text = f.read()

old_str = """      body: JSON.stringify({
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
      throw new Error(`Airtable Error: ${JSON.stringify(errorData)}`);
    }

    // Success
    return res.status(200).json({ success: true, message: 'Lead added to CRM' });

  } catch (error) {
    console.error('Submission Error:', error);
    return res.status(500).json({ error: 'Failed to process lead submission' });
  }
}"""

new_str = """      body: JSON.stringify({
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
}"""

with open("api/submit-lead.js", "w", encoding="utf-8") as f:
    f.write(text.replace(old_str, new_str))
