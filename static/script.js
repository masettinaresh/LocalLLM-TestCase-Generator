document.getElementById('generateBtn').addEventListener('click', async () => {
    const userInput = document.getElementById('userInput').value.trim();
    if (!userInput) return alert("Please enter requirements.");

    // UI Loading State
    const btn = document.getElementById('generateBtn');
    const btnText = document.getElementById('btnText');
    const loader = document.getElementById('loader');
    const outputSection = document.getElementById('outputSection');
    const resultContent = document.getElementById('resultContent');

    btn.disabled = true;
    btnText.textContent = "Generating...";
    loader.style.display = "block";
    outputSection.style.display = "none";
    resultContent.innerHTML = "";

    try {
        const response = await fetch('/api/generate', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ user_input: userInput })
        });

        const data = await response.json();

        if (data.error) {
            throw new Error(data.error);
        }

        // Render Markdown
        resultContent.innerHTML = marked.parse(data.generated_testcases);
        outputSection.style.display = "block";

    } catch (error) {
        alert("Error: " + error.message);
    } finally {
        btn.disabled = false;
        btnText.textContent = "Generate Test Cases";
        loader.style.display = "none";
    }
});

function copyToClipboard() {
    const content = document.getElementById('resultContent').innerText;
    navigator.clipboard.writeText(content).then(() => {
        const copyBtn = document.querySelector('.copy-btn:last-child'); // Target the copy button
        const originalText = copyBtn.innerText;
        copyBtn.innerText = "Copied!";
        setTimeout(() => copyBtn.innerText = originalText, 2000);
    });
}

function downloadReport() {
    const content = document.getElementById('resultContent').innerText;
    const blob = new Blob([content], { type: 'text/markdown' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'test_cases.md';
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
}
