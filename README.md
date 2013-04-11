yum-plugin-appendinstallonly
============================

A plugin for yum which will add to the installonlypkgs directive without
overwritting what's in /etc/yum.conf or overriding the defaults contained
in yum's config.py code

Work in progress... stay tuned, or something... :)

# How To Use

Place appendinstallonly.py in /usr/lib/yum-plugins/ and appendinstallonly.conf
in /etc/yum/pluginconf.d/ and add packages to the appendinstallonly directive.
Packages can be listed in either comma or whitespace delimited notation.

Example:

    
    [main]
    enabled=1
    appendinstallonlypkgs=openshift-origin-cartridge-python,
                            openshift-origin-cartridge-ruby
    

