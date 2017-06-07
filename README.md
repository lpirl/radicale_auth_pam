# Radicale Auth Module : PAM

This is an auth module for [Radicale](http://radicale.org/) >= 2.0.

## Purpose

This module allows Radicale to entrust users that can authenticate against PAM. This way, you can rely on local logins for authentication (e.g., because you have an
email server running that relies on local logins anyway) and use Radicale's rights management for fine-grained control.

## How does it work

As a Radicale auth module it's only suppose to provide authentication means for a given user.
This module will check the provided user name and password with PAM (using the package ``python-pam``).

## How to use it

Install this module through `pip` with :

`pip3 install ./radicale_auth_pam`

Then, edit the radicale configuration file (most likely `/etc/radicale/config`, and change the `type` setting in the `[auth]` section :

```config
[auth]
type = radicale_auth_pam
```

Make sure the user that runs Radicale can access ``/etc/shadow``.
For the version of Radicale packaged in Debian, you'd need to add the user
``radical`` to the group ``shadow``:

```$ usermod -aG shadow radicale```

## Maturity status

I used this plugin a few hours to test Radicale and it worked, should be pretty solid. ;)
