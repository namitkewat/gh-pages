Title: My First experiance with Vagrant
Date: 2015-08-22 12:22
Author: namitkewat
Category: General
Slug: my-first-experiance-with-vagrant
Status: published

Last week, I have faced some internet issue with my ISP. So in free
time; i spent some time exploring vagrant boxes with its command line
help and followed the instruction to setup the box. I have earlier tried
that but that was followed using some online post and didn't remember
those steps. So command line help was useful.

Setup is very easy. It will take just few minutes. I have recorded the
step. Those are below:

```bash
Microsoft Windows [Version 6.3.9600]  
(c) 2013 Microsoft Corporation. All rights reserved.

C:\\Users\\namitkewat\>vagrant box --help  
Usage: vagrant box \<subcommand\> [\<args\>]

Available subcommands:  
add  
list  
outdated  
remove  
repackage  
update

For help on any individual subcommand run \`vagrant box
\<subcommand\> -h\`

C:\\Users\\namitkewat\>vagrant box add --help  
Usage: vagrant box add [options] \<name, url, or path\>

Options:

-c, --clean Clean any temporary download files  
-f, --force Overwrite an existing box if it exists  
--insecure Do not validate SSL certificates  
--cacert FILE CA certificate for SSL download  
--capath DIR CA certificate directory for SSL download  
--cert FILE A client SSL cert, if needed  
--location-trusted Trust 'Location' header from HTTP redirects  
and use the same credentials for subsequent urls as for the initial
one  
--provider PROVIDER Provider the box should satisfy  
--box-version VERSION Constrain version of the added box

The box descriptor can be the name of a box on HashiCorp's Atlas,  
or a URL, or a local .box file, or a local .json file containing  
the catalog metadata.

The options below only apply if you're adding a box file directly,  
and not using a Vagrant server or a box structured like 'user/box':

--checksum CHECKSUM Checksum for the box  
--checksum-type TYPE Checksum type (md5, sha1, sha256)  
--name BOX Name of the box  
-h, --help Print this help

C:\\Users\\namitkewat\>vagrant box add
F:\\ubuntu-14.04-amd64-vbox.box --name ubuntu  
1404  
==\> box: Box file was not detected as metadata. Adding it directly...  
==\> box: Adding box 'ubuntu1404' (v0) for provider:  
box: Unpacking necessary files from:
file://F:/ubuntu-14.04-amd64-vbox.box  
box:  
An error occurred while downloading the remote file. The error  
message, if any, is reproduced below. Please fix this error and try  
again.

Couldn't open file /ubuntu-14.04-amd64-vbox.box

C:\\Users\\namitkewat\>F:

F:\\\>vagrant box add ubuntu-14.04-amd64-vbox.box --name ubuntu1404  
==\> box: Box file was not detected as metadata. Adding it directly...  
==\> box: Adding box 'ubuntu1404' (v0) for provider:  
box: Unpacking necessary files from:
file://F:/ubuntu-14.04-amd64-vbox.box  
box: Progress: 100% (Rate: 615M/s, Estimated time remaining: --:--:--)  
==\> box: Successfully added box 'ubuntu1404' (v0) for 'virtualbox'!

F:\\\>mkdir vagrant\_work

F:\\\>cd vagrant\_work

F:\\vagrant\_work\>mkdir ubuntu1404

F:\\vagrant\_work\>cd ubuntu1404

F:\\vagrant\_work\\ubuntu1404\>vagrant init ubuntu1404  
A \`Vagrantfile\` has been placed in this directory. You are now  
ready to \`vagrant up\` your first virtual environment! Please read  
the comments in the Vagrantfile as well as documentation on  
\`vagrantup.com\` for more information on using Vagrant.

F:\\vagrant\_work\\ubuntu1404\>dir  
Volume in drive F has no label.  
Volume Serial Number is 5AFD-1ED3

Directory of F:\\vagrant\_work\\ubuntu1404

09-08-2015 16:03 \<DIR\> .  
09-08-2015 16:03 \<DIR\> ..  
09-08-2015 16:03 3,093 Vagrantfile  
1 File(s) 3,093 bytes  
2 Dir(s) 210,471,010,304 bytes free

F:\\vagrant\_work\\ubuntu1404\>vagrant up  
Bringing machine 'default' up with 'virtualbox' provider...  
==\> default: Importing base box 'ubuntu1404'...  
==\> default: Matching MAC address for NAT networking...  
==\> default: Setting the name of the VM:
ubuntu1404\_default\_1439116510430\_18589  
==\> default: Clearing any previously set forwarded ports...  
==\> default: Clearing any previously set network interfaces...  
==\> default: Preparing network interfaces based on configuration...  
default: Adapter 1: nat  
==\> default: Forwarding ports...  
default: 22 =\> 2222 (adapter 1)  
==\> default: Booting VM...  
==\> default: Waiting for machine to boot. This may take a few
minutes...  
default: SSH address: 127.0.0.1:2222  
default: SSH username: vagrant  
default: SSH auth method: private key  
default: Warning: Connection timeout. Retrying...  
default:  
default: Vagrant insecure key detected. Vagrant will automatically
replace  
default: this with a newly generated keypair for better security.  
default:  
default: Inserting generated public key within guest...  
default: Removing insecure key from the guest if it's present...  
default: Key inserted! Disconnecting and reconnecting using new SSH
key...  
==\> default: Machine booted and ready!  
==\> default: Checking for guest additions in VM...  
==\> default: Mounting shared folders...  
default: /vagrant =\> F:/vagrant\_work/ubuntu1404

F:\\vagrant\_work\\ubuntu1404\>
```
