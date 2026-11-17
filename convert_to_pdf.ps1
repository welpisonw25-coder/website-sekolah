try {
    $word = New-Object -ComObject Word.Application
    $word.Visible = $false
    Write-Output "Word COM is installed!"
    $docPath = "c:\Users\acer\Documents\WEBSITE-SEKOLAH-SD INPRES ARSO 8\BAHAN_PRESENTASI_DAN_PANDUAN_SERAH_TERIMA_SDN_ARSO_8.docx"
    $pdfPath = "c:\Users\acer\Documents\WEBSITE-SEKOLAH-SD INPRES ARSO 8\BAHAN_PRESENTASI_DAN_PANDUAN_SERAH_TERIMA_SDN_ARSO_8.pdf"
    $doc = $word.Documents.Open($docPath)
    # 17 represents wdExportFormatPDF
    $doc.SaveAs([ref]$pdfPath, [ref]17)
    $doc.Close()
    $word.Quit()
    Write-Output "PDF converted successfully!"
} catch {
    Write-Output "Error: $_"
}
