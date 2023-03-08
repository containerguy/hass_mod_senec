
#!/usr/local/microsoft/powershell/7/pwsh
<#
This script will download all log files starting at the refdarte (install date of your senec battery system) to the current directory. all files will be named with pattern 'yyyy-MM-dd'

#>
$senec_ip = "192.168.123.41"
$refdate= get-date -date "2022-02-07"
$days = [Math]::truncate(((get-date) - ($refdate)).totaldays)
for ($i=1;$i -le $days;$i++) {$incdate = $incdate.AddDays(1); curl -o "$($incdate.Year)-$($incdate.month.ToString('00'))-$($incdate.day.ToString('00')).log" http://$senec_ip/log/$($incdate.year)/$($incdate.month.ToString('00'))/$($incdate.day.ToString('00')).log }
