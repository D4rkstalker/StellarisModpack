#Made by 'The Dadinator', the Author of 'EAC: At War' Mod. #Edited by me, 'XVCV' with 'ChatGPT 4.0'

try
{
    Set-Location -Path "english" -ErrorAction Stop
    $sourceDirectory = "$PWD"
    $languages = @{"braz_por" = "l_braz_por"; "french" = "l_french"; "german" = "l_german"; "polish" = "l_polish"; "russian" = "l_russian"; "spanish" = "l_spanish"; "simp_chinese" = "l_simp_chinese"; "japanese" = "l_japanese"}
    $language = ""

    foreach($folderName in $($languages.keys)){
        $language = $languages[$folderName]
        $targetDirectory = $sourceDirectory.Replace("english", $folderName)

        #Delete Existing Language Files
        if(Test-Path $targetDirectory){
            Remove-Item -Recurse -Force $targetDirectory -ErrorAction Stop
        }

        #Copy English Files
        Copy-Item $sourceDirectory $targetDirectory -recurse -ErrorAction Stop

        #Change to the directory
        Set-Location -Path $targetDirectory -ErrorAction Stop

        #Rename Files
        Get-ChildItem -Recurse -file | 
            ForEach-Object{
                Rename-Item -Path $_.Fullname -NewName $_.Name.Replace("l_english",$language) -ErrorAction Stop
            }

        #Replace in Files
        $configFiles = Get-ChildItem . *.yml -Recurse
        foreach ($file in $configFiles)
        {
            (Get-Content $file.PSPath) |
            Foreach-Object { $_ -replace "l_english", "$language" } |
            Set-Content $file.PSPath -encoding UTF8 -ErrorAction Stop
        }
    }
}
catch
{
    Write-Host "An error occurred: $_" -ForegroundColor Red
}