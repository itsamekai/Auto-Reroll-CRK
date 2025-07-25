function Find-VenvFolder {
    $current = Get-Location

    while ($current -ne $null) {
        $venvPath = Join-Path $current "venv"
        if (Test-Path $venvPath) {
            return $venvPath
        }
        $current = $current.Parent
    }
    return $null
}

$venvFolder = Find-VenvFolder

if (-not $venvFolder) {
    Write-Error "no venv dir found."
    exit 1
}

Write-Host "Found venv at: $venvFolder"

& "$venvFolder\Scripts\Activate.ps1"

Write-Host "building app."
pyinstaller --onedir --add-data "Tesseract-OCR;Tesseract-OCR" main.py
Write-Host "completed." 