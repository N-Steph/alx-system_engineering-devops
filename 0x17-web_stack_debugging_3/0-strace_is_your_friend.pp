exec { 'fix_phpp_extension':
  command => "/bin/sed -i 's/\\.phpp/.php/g' /var/www/html/wp-settings.php",
  onlyif  => "/bin/grep -q '\\.phpp' /var/www/html/wp-settings.php",
}