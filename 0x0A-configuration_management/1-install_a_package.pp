# install puppet-lint using puppet
package { 'puppet-lint':
  ensure   => 'installed'
}
exec { 'puppet-lint':
    command => 'gem install puppet-lint -v 2.1.1'
}
