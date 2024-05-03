# PowerShell script to check and set the startup type of a service

# Define the service name
$serviceName = "DellClientManagementService"

# Get the current startup type of the service
$currentStartupType = Get-WmiObject -Class Win32_Service -Filter "Name = '$serviceName'" | Select-Object -ExpandProperty StartMode
Write-Host "Current Startup Type of ${serviceName}: $currentStartupType"

# Set the startup type to Automatic if it is not already set
if ($currentStartupType -ne "Auto") {
    Set-Service -Name $serviceName -StartupType Automatic
    Write-Host "Startup type set to Automatic for ${serviceName}."
} else {
    Write-Host "The startup type is already set to Automatic."
}
