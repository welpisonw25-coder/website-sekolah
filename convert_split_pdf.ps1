try {
    $word = New-Object -ComObject Word.Application
    $word.Visible = $false
    
    $files = @(
        @{
            docx = "c:\Users\acer\Documents\WEBSITE-SEKOLAH-SD INPRES ARSO 8\1_MATERI_PRESENTASI_WEBSITE_SDN_INPRES_ARSO_8.docx"
            pdf  = "c:\Users\acer\Documents\WEBSITE-SEKOLAH-SD INPRES ARSO 8\1_MATERI_PRESENTASI_WEBSITE_SDN_INPRES_ARSO_8.pdf"
            dl_docx = "c:\Users\acer\Downloads\1_MATERI_PRESENTASI_WEBSITE_SDN_INPRES_ARSO_8.docx"
            dl_pdf  = "c:\Users\acer\Downloads\1_MATERI_PRESENTASI_WEBSITE_SDN_INPRES_ARSO_8.pdf"
        },
        @{
            docx = "c:\Users\acer\Documents\WEBSITE-SEKOLAH-SD INPRES ARSO 8\2_BERITA_ACARA_SERAH_TERIMA_WEBSITE_SDN_INPRES_ARSO_8.docx"
            pdf  = "c:\Users\acer\Documents\WEBSITE-SEKOLAH-SD INPRES ARSO 8\2_BERITA_ACARA_SERAH_TERIMA_WEBSITE_SDN_INPRES_ARSO_8.pdf"
            dl_docx = "c:\Users\acer\Downloads\2_BERITA_ACARA_SERAH_TERIMA_WEBSITE_SDN_INPRES_ARSO_8.docx"
            dl_pdf  = "c:\Users\acer\Downloads\2_BERITA_ACARA_SERAH_TERIMA_WEBSITE_SDN_INPRES_ARSO_8.pdf"
        }
    )

    foreach ($item in $files) {
        Write-Output "Converting $($item.docx)..."
        $doc = $word.Documents.Open($item.docx)
        $doc.SaveAs([ref]$item.pdf, [ref]17)
        $doc.Close()
        Copy-Item $item.pdf $item.dl_pdf -Force
        Write-Output "Generated and copied: $($item.dl_pdf)"
    }
    
    $word.Quit()
    Write-Output "All PDF documents created successfully!"
} catch {
    Write-Output "Error: $_"
}
