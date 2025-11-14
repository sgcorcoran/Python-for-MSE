# Setting Up Anonymous Survey in Microsoft Forms

## Step-by-Step Instructions

### 1. Create New Form
- Go to Microsoft Forms (forms.microsoft.com or via Office 365)
- Click "New Form"
- Name it: "MSE 3114: Mid-Course Evaluation Survey"

### 2. Enable Anonymous Responses (CRITICAL STEP)
**This is the key setting for anonymity:**

1. Click the **three dots (⋮)** menu in the top right
2. Select **"Settings"**
3. Under **"Who can fill out this form"**:
   - Select **"Anyone with the link can respond"** 
4. Under **"Settings"**, check/uncheck:
   - ✅ **"One response per person"** - UNCHECK this (allows true anonymity)
   - ✅ **"Record name"** - Make sure this is OFF/UNCHECKED
   - ✅ **"Show results automatically"** - Your choice (usually leave OFF)

### 3. Privacy Settings
- Go to **Form Settings** (three dots menu)
- Ensure **"Collect respondent names"** is OFF/UNCHECKED
- This ensures responses are truly anonymous

### 4. Add Questions
Copy questions from `SURVEY_GOOGLE_FORMS_VERSION.txt` or `MSE3114_Mid_Course_Evaluation_Survey.md`

**Question Type Mapping:**
- Q1-Q4, Q7-Q8: **Choice** → **Radio buttons** (single answer)
- Q5, Q6, Q9, Q10: **Choice** → **Multiple choice with checkboxes** (multiple answers)
- Q11: **Choice** → **Multiple choice with checkboxes** (set limit to 2)
  - To set limit: In question settings, enable "Limit number of selections" and set to 2
- Q12-Q15: **Text** → **Long answer** (paragraph format)

### 5. Important Notes for Anonymity

#### What Microsoft Forms DOES:
✅ Does NOT collect names by default (if settings are correct)
✅ Does NOT require sign-in (if "Anyone with the link" is selected)
✅ Responses are anonymous to respondents
✅ You won't see who submitted which response

#### What Microsoft Forms CANNOT Do:
⚠️ **If you enable "One response per person"** - Microsoft can track duplicates using browser/device info (but still not names)
⚠️ **If you share via Microsoft 365** - The system might log organizational info (if using VT email)
⚠️ **IP addresses** - Microsoft may log IP addresses for security, but these aren't shown in results

### 6. Best Practices for Maximum Anonymity

#### Option A: Fully Anonymous (Recommended)
1. Create form with settings:
   - ✅ "Anyone with the link can respond"
   - ✅ "One response per person" - **UNCHECKED**
   - ✅ "Collect respondent names" - **OFF**
   - ✅ "Record name" - **OFF**
2. Share via **anonymous link** (not through Canvas or email with name tracking)
3. Optionally share link via:
   - Anonymous QR code in class
   - Anonymous URL shortener
   - Posted on course page (students click themselves)

#### Option B: Semi-Anonymous (If you need to track completion)
1. Enable "One response per person" - allows duplicate detection but doesn't show names
2. Still anonymous to you (no names visible)
3. You can see if someone submits multiple times

### 7. How to Share the Survey

**For Maximum Anonymity:**
1. Get the **shareable link** from Forms
2. Options:
   - Create QR code (scan in class - no tracking)
   - Post link on Canvas course page (students navigate themselves)
   - Share via anonymous URL shortener
   - Project link on screen in class (students type it in)

**What to AVOID:**
- ❌ Don't require students to sign in to Microsoft
- ❌ Don't send link via email that requires authentication
- ❌ Don't use "Only people in my organization" if you want true anonymity

### 8. Verifying Anonymity

**Before distributing:**
1. Test the form yourself (open in incognito/private browser)
2. Submit a test response
3. Check results - you should NOT see:
   - Names
   - Email addresses
   - Organizational identifiers
4. You should only see:
   - Response timestamps (can disable if desired)
   - Response data (answers)

**To disable timestamps:**
- Go to Form Settings
- Under "Settings" tab
- Uncheck "Show response submission date and time" (if available)

### 9. Collecting Results

**Viewing Results:**
- Click "Responses" tab in your form
- You'll see summary statistics
- Individual responses can be viewed (but no names)
- Export to Excel if needed for analysis

**Data Export:**
- Click "Open in Excel" in Responses tab
- Export contains all responses but NO identifying information (if set up correctly)

---

## Summary: Key Settings for Anonymity

✅ **Enable:**
- "Anyone with the link can respond"
- All questions visible
- Form sharing enabled

❌ **Disable:**
- "One response per person" (for true anonymity - optional)
- "Collect respondent names" 
- "Record name"
- Any authentication requirements

✅ **Result:**
- Truly anonymous responses
- No names collected
- No sign-in required
- Responses can't be traced to individuals

---

## Troubleshooting

**Issue: Form requires sign-in**
→ Solution: Change "Who can fill out" to "Anyone with the link"

**Issue: I see names in responses**
→ Solution: Check Settings → "Collect respondent names" is OFF

**Issue: Students say they need to sign in**
→ Solution: They may be using a different link - provide the direct anonymous link

**Issue: Need to prevent multiple submissions**
→ Solution: Enable "One response per person" (reduces anonymity slightly but still no names)

---

## Additional Privacy Notes

**Microsoft Forms Privacy:**
- Microsoft may log metadata (IP addresses, timestamps) for security
- These logs are NOT visible in your form results
- Microsoft doesn't share this with form owners for anonymous surveys
- Compliance: Microsoft Forms complies with FERPA when used by educational institutions

**For VT/Virginia Tech:**
- Check VT IT policies regarding Microsoft 365 usage
- Generally, anonymous surveys are permitted for course evaluations
- Consider if there are any department-specific requirements

---

## Quick Setup Checklist

- [ ] Form created
- [ ] Settings → "Anyone with the link" enabled
- [ ] Settings → "Collect names" DISABLED
- [ ] Settings → "One response per person" UNCHECKED (for full anonymity)
- [ ] All 15 questions added
- [ ] Multiple-choice questions set to allow multiple answers where needed
- [ ] Q11 set to limit 2 selections
- [ ] Test response submitted (verify no names appear)
- [ ] Anonymous share link obtained
- [ ] Link ready to share with class

---

**Your survey will be anonymous as long as these settings are correct!**

