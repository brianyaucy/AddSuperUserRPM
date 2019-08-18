# Description
This repo contains source code of AddSuperUser RPM.

The RPM is used to deal with situation where a user can run yum as sudo, and you want to perform privilege escalation. 

If so, you can build this RPM and install this RPM on the target. By doing so, the commands in SPECS/addsuperuser.spec will be run, leading to:

- Adding a user "superuser" without password, with userid and groupid being 0
- Do setuid for /bin/vim, /bin/nano and /bin/vi

When switching user to superuser after installing the rpm, you will be root!

# Build

In the root directory of this repo, do:

```
# rpmbuild -ba SPECS/addsuperuser.spec 
```

Then the RPM file will be created in /root/rpmbuild/RPMS/noarch/addsuperuser-1-0.noarch.rpm
