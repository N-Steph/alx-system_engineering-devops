# manifest that kills a process named killmenow

exec { 'pkill -f killmenow':
command => '/usr/bin/pkill -f killmenow'
}
