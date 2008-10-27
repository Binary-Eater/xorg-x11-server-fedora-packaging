# This package is an experiment in active integration of upstream SCM with
# Fedora packaging.  It works something like this:
#
# The "pristine" source is actually a git repo (with no working checkout).
# The first step of %%prep is to check it out and switch to a "fedora" branch.
# If you need to add a patch to the server, just do it like a normal git
# operation, dump it with git-format-patch to a file in the standard naming
# format, and add a PatchN: line.  If you want to push something upstream,
# check out the master branch, pull, cherry-pick, and push.  FIXME describe
# rebasing, add convenience 'make' targets maybe.

# F10 TODO list:
#
# Fix rhpxl to no longer need vesamodes/extramodes

%define pkgname xorg-server
#define gitdate 20080701

Summary:   X.Org X11 X server
Name:      xorg-x11-server
Version:   1.5.2
Release:   9%{?dist}
URL:       http://www.x.org
License:   MIT
Group:     User Interface/X
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%if 0%{?gitdate}
# git snapshot.  to recreate, run:
# ./make-git-snapshot.sh `cat commitid`
Source0:   xorg-server-%{gitdate}.tar.bz2
Source1:   make-git-snapshot.sh
Source2:   commitid
%else
Source0:   http://www.x.org/pub/individual/xserver/%{pkgname}-%{version}.tar.bz2
Source1:   gitignore
%endif

# keyboard enablement
Source10:  10-x11-keymap.fdi
Source11:  fedora-setup-keyboard

# Useful xvfb-run script
Source20:  http://svn.exactcode.de/t2/trunk/package/xorg/xorg-server/xvfb-run.sh

# OpenGL compositing manager feature/optimization patches.
Patch100:  xorg-x11-server-1.1.0-no-move-damage.patch
Patch101:  xserver-1.4.99-dont-backfill-bg-none.patch
# XXX does this need rebasing still?
Patch102:  xserver-1.5.0-exa-master-upgrade.patch
Patch103:  xserver-1.5.0-bg-none-root.patch
Patch104:  xserver-1.5.0-exa-master-fix-x11perf-crash.patch
Patch105:  xserver-1.5.1-exa-fix-glyph-segfault.patch

# Red Hat specific tweaking, not intended for upstream
# XXX move these to the end of the list
Patch1003:  xserver-1.4.99-pic-libxf86config.patch
Patch1005:  xserver-1.4.99-builtin-fonts.patch

Patch2013:  xserver-1.4.99-document-fontpath-correctly.patch
Patch2014:  xserver-1.5.0-projector-fb-size.patch

# Trivial things to never merge upstream ever
# Don't merge this without protecting the gccisms.
Patch5001:  xserver-1.4.99-alloca-poison.patch
# This really could be done prettier.
Patch5002:  xserver-1.4.99-ssh-isnt-local.patch
Patch5003:  xserver-1.5.1-xgi.patch

Patch5007:  xserver-1.5.0-bad-fbdev-thats-mine.patch

# Workaround RH bug #449944
Patch5011: xserver-1.4.99-endian.patch

# evdev keyboard map fix
#Patch5013: xserver-1.5.0-xkb-fix-ProcXkbSetXYZ-to-work-on-all.patch
Patch5013: xserver-1.5.0-force-SwitchCoreKeyboard-for-evdev.patch
# Patch5015: xserver-1.5.0-enable-selinux.patch
Patch6000: xserver-1.5.0-hide-cursor.patch
Patch6001: xserver-1.5.0-edid-backport.patch

# force mode debugging on for randr 1.2 drivers
Patch6003: xserver-1.5.1-mode-debug.patch

Patch6004: xserver-1.5.1-global-backtrace.patch
Patch6005: xserver-1.5.2-mieq-backtrace.patch
Patch6006: xserver-1.5.2-backtrace-defines.patch
Patch6007: xserver-1.5.2-lies-damn-lies-and-aspect-ratios.patch

# No evdev grab, disable kbd/mouse
Patch6008: xserver-1.5.2-enable-RAW-console.patch
Patch6009: xserver-1.5.2-disable-kbd-mouse.patch
Patch6010: xserver-1.5.2-no-duplicate-devices.patch

# exa performance fix
Patch6011: xserver-1.5.2-exa-sync-less.patch

# Bug 434807
Patch6012: xserver-1.5.2-more-sanity-checks.patch

%define moduledir	%{_libdir}/xorg/modules
%define drimoduledir	%{_libdir}/dri
%define sdkdir		%{_includedir}/xorg

%ifarch s390 s390x
%define with_hw_servers 0
%else
%define with_hw_servers 1
%endif

%if %{with_hw_servers}
%define enable_xorg --enable-xorg
%else
%define enable_xorg --disable-xorg
%endif

%define kdrive --enable-kdrive --enable-xephyr --disable-xsdl --disable-xfake --disable-xfbdev --disable-kdrive-vesa
%define xservers --enable-xvfb --enable-xnest %{kdrive} %{enable_xorg} --enable-dmx

BuildRequires: git-core
BuildRequires: automake autoconf libtool pkgconfig
BuildRequires: xorg-x11-util-macros >= 1.1.5

BuildRequires: xorg-x11-proto-devel >= 7.4-3
BuildRequires: damageproto >= 1.1
BuildRequires: dri2proto >= 1.99.1
BuildRequires: fixesproto >= 4.0
BuildRequires: glproto >= 1.4.9
BuildRequires: kbproto >= 1.0.3
BuildRequires: randrproto >= 1.2
BuildRequires: renderproto >= 0.9.3
BuildRequires: scrnsaverproto >= 1.1

BuildRequires: xorg-x11-xtrans-devel >= 1.0.3-3
BuildRequires: libXfont-devel libXau-devel libxkbfile-devel libXres-devel
BuildRequires: libfontenc-devel libXtst-devel libXdmcp-devel
BuildRequires: libX11-devel libXext-devel

# DMX config utils buildreqs.
BuildRequires: libXt-devel libdmx-devel libXmu-devel libXrender-devel
BuildRequires: libXi-devel libXpm-devel libXaw-devel libXfixes-devel

# Broken, this is global, should be Xephyr-only
BuildRequires: libXv-devel

# openssl? really?
BuildRequires: pixman-devel libpciaccess-devel openssl-devel byacc flex
BuildRequires: mesa-libGL-devel >= 7.1-0.37
# should be useless now...
# BuildRequires: mesa-source >= 7.1-0.36
# XXX silly...
BuildRequires: libdrm-devel >= 2.4.0 kernel-devel
%if %{with_hw_servers}
Requires: libdrm >= 2.4.0
%endif

BuildRequires: audit-libs-devel libselinux-devel >= 2.0.59-1
BuildRequires: hal-devel dbus-devel

# All server subpackages have a virtual provide for the name of the server
# they deliver.  The Xorg one is versioned, the others are intentionally
# unversioned.

%description
X.Org X11 X server

%package common
Summary: Xorg server common files
Group: User Interface/X

%description common
Common files shared among all X servers.

%if %{with_hw_servers}
%package Xorg
Summary: Xorg X server
Group: User Interface/X
Provides: Xorg = %{version}-%{release}
Provides: Xserver
# Requires: xorg-x11-drivers >= 0.99.2-4
Requires: xorg-x11-drv-mouse xorg-x11-drv-keyboard xorg-x11-drv-vesa
Requires: xorg-x11-drv-void xorg-x11-drv-evdev
# virtuals.  XXX fix the xkbcomp fork() upstream.
Requires: xkbdata xkbcomp
Requires: xorg-x11-server-common >= %{version}-%{release}
# These drivers were dropped in F7 for being broken, so uninstall them.
Obsoletes: xorg-x11-drv-elo2300 <= 1.1.0-2.fc7
Obsoletes: xorg-x11-drv-joystick <= 1.1.0-2.fc7
# Dropped from F9 for being broken, uninstall it.
Obsoletes: xorg-x11-drv-magictouch <= 1.0.0.5-5.fc8
# Force sufficiently new libpciaccess
Conflicts: libpciaccess < 0.9.1-2

%description Xorg
X.org X11 is an open source implementation of the X Window System.  It
provides the basic low level functionality which full fledged
graphical user interfaces (GUIs) such as GNOME and KDE are designed
upon.
%endif


%package Xnest
Summary: A nested server.
Group: User Interface/X
Obsoletes: xorg-x11-Xnest
Requires: xorg-x11-server-common >= %{version}-%{release}
Provides: Xnest

%description Xnest
Xnest is an X server, which has been implemented as an ordinary
X application.  It runs in a window just like other X applications,
but it is an X server itself in which you can run other software.  It
is a very useful tool for developers who wish to test their
applications without running them on their real X server.


%package Xdmx
Summary: Distributed Multihead X Server and utilities
Group: User Interface/X
Obsoletes: xorg-x11-Xdmx
Requires: xorg-x11-server-common >= %{version}-%{release}
Provides: Xdmx

%description Xdmx
Xdmx is proxy X server that provides multi-head support for multiple displays
attached to different machines (each of which is running a typical X server).
When Xinerama is used with Xdmx, the multiple displays on multiple machines
are presented to the user as a single unified screen.  A simple application
for Xdmx would be to provide multi-head support using two desktop machines,
each of which has a single display device attached to it.  A complex
application for Xdmx would be to unify a 4 by 4 grid of 1280x1024 displays
(each attached to one of 16 computers) into a unified 5120x4096 display.


%package Xvfb
Summary: A X Windows System virtual framebuffer X server.
Group: User Interface/X
# xvfb-run is GPLv2, rest is MIT
License: MIT and GPLv2
Obsoletes: xorg-x11-Xvfb
Requires: xorg-x11-server-common >= %{version}-%{release}
Provides: Xvfb

%description Xvfb
Xvfb (X Virtual Frame Buffer) is an X server that is able to run on
machines with no display hardware and no physical input devices.
Xvfb simulates a dumb framebuffer using virtual memory.  Xvfb does
not open any devices, but behaves otherwise as an X display.  Xvfb
is normally used for testing servers.


%package Xephyr
Summary: A nested server.
Group: User Interface/X
Requires: xorg-x11-server-common >= %{version}-%{release}
Provides: Xephyr

%description Xephyr
Xephyr is an X server, which has been implemented as an ordinary
X application.  It runs in a window just like other X applications,
but it is an X server itself in which you can run other software.  It
is a very useful tool for developers who wish to test their
applications without running them on their real X server.  Unlike
Xnest, Xephyr renders to an X image rather than relaying the
X protocol, and therefore supports the newer X extensions like
Render and Composite.


%if %{with_hw_servers}
%package devel
Summary: SDK for X server driver module development
Group: User Interface/X
Obsoletes: xorg-x11-sdk xorg-x11-server-sdk
Requires: xorg-x11-util-macros
Requires: xorg-x11-proto-devel
Requires: pkgconfig pixman-devel libpciaccess-devel
Requires(pre): xorg-x11-filesystem >= 0.99.2-3
Provides: libxf86config-devel = %{version}-%{release}
# Virtual provide for transition.  Delete me someday.
Provides: xorg-x11-server-sdk = %{version}-%{release}

%description devel
The SDK package provides the developmental files which are necessary for
developing X server driver modules, and for compiling driver modules
outside of the standard X11 source code tree.  Developers writing video
drivers, input drivers, or other X modules should install this package.
%endif

%package source
Summary: Xserver source code required to build VNC server (Xvnc)
Group: Development/Libraries

%description source
Xserver source code needed to build VNC server (Xvnc)

%prep
%setup -q -n %{pkgname}-%{?gitdate:%{gitdate}}%{!?gitdate:%{version}}

%if 0%{?gitdate}
git checkout -b fedora
sed -i 's/git/&+ssh/' .git/config
%else
git-init-db
if [ -z "$GIT_COMMITTER_NAME" ]; then
    git-config user.email "x@fedoraproject.org"
    git-config user.name "Fedora X Ninjas"
fi
cp %{SOURCE1} .gitignore
git-add .
git-commit -a -q -m "%{version} baseline."
%endif

# Apply all the patches.
#git-am -p1 %{patches}
git-am -p1 $(awk '/^Patch.*:/ { print "%{_sourcedir}/"$2 }' %{_specdir}/%{name}.spec)

%build

%define default_font_path "catalogue:/etc/X11/fontpath.d,built-ins"

# --with-rgb-path should be superfluous now ?
# --with-pie ?
autoreconf -v --install || exit 1
export CFLAGS="${RPM_OPT_FLAGS} -Wstrict-overflow -rdynamic $CFLAGS"
%configure --enable-maintainer-mode %{xservers} \
	--disable-static \
	--with-pic \
	--disable-{a,c,m}fb \
	--with-int10=x86emu \
	--with-default-font-path=%{default_font_path} \
	--with-module-dir=%{moduledir} \
	--with-builderstring="Build ID: %{name} %{version}-%{release}" \
	--with-xkb-output=%{_localstatedir}/lib/xkb \
	--with-rgb-path=%{_datadir}/X11/rgb \
	--disable-xorgcfg \
	--disable-record --disable-xtrap \
	--enable-install-libxf86config \
	--enable-xselinux \
	--with-dri-driver-path=%{drimoduledir} \
	--disable-dri2 \
	${CONFIGURE}

make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT moduledir=%{moduledir}

%if %{with_hw_servers}
mkdir -p $RPM_BUILD_ROOT%{_libdir}/xorg/modules/{drivers,input}

# Install the vesamodes and extramodes files to let our install/config tools
# be able to parse the same modelist as the X server uses (rhpxl).
mkdir -p $RPM_BUILD_ROOT%{_datadir}/xorg
install -m 0444 hw/xfree86/common/{vesa,extra}modes $RPM_BUILD_ROOT%{_datadir}/xorg/

# fedora-isms to slurp keyboard settings out of /etc/sysconfig/keyboard
mkdir -p $RPM_BUILD_ROOT%{_datadir}/hal/fdi/policy/10osvendor
install -m 0444 %{SOURCE10} $RPM_BUILD_ROOT%{_datadir}/hal/fdi/policy/10osvendor
install -m 0755 %{SOURCE11} $RPM_BUILD_ROOT%{_bindir}
%endif

# Make the source package
%define xserver_source_dir %{_datadir}/xorg-x11-server-source
%define inst_srcdir %{buildroot}/%{xserver_source_dir}
mkdir -p %{inst_srcdir}/{Xext,xkb,GL,hw/xfree86/{common,utils/xorgconfig}}
cp cpprules.in %{inst_srcdir}
cp xkb/README.compiled %{inst_srcdir}/xkb
cp hw/xfree86/{xorgconf.cpp,Options} %{inst_srcdir}/hw/xfree86
cp hw/xfree86/common/{vesamodes,extramodes} %{inst_srcdir}/hw/xfree86/common
cp hw/xfree86/utils/xorgconfig/Cards{,98} %{inst_srcdir}/hw/xfree86/utils/xorgconfig/

install -m 0755 %{SOURCE20} $RPM_BUILD_ROOT%{_bindir}/xvfb-run

find . -type f | egrep '.*\.(c|h|am|ac|inc|m4|h.in|pc.in|man.pre|pl|txt)$' |
xargs tar cf - | (cd %{inst_srcdir} && tar xf -)

# Remove unwanted files/dirs
{
    rm -f $RPM_BUILD_ROOT%{_bindir}/xorgconfig
    rm -f $RPM_BUILD_ROOT%{_mandir}/man1/xorgconfig.1*
    rm -f $RPM_BUILD_ROOT%{_libdir}/X11/Cards
    rm -f $RPM_BUILD_ROOT%{_libdir}/X11/Options
    rm -f $RPM_BUILD_ROOT%{_bindir}/in?
    rm -f $RPM_BUILD_ROOT%{_bindir}/ioport
    rm -f $RPM_BUILD_ROOT%{_bindir}/out?
    rm -f $RPM_BUILD_ROOT%{_bindir}/pcitweak
    rm -f $RPM_BUILD_ROOT%{_mandir}/man1/pcitweak.1*
    find $RPM_BUILD_ROOT -type f -name '*.la' | xargs rm -f -- || :
}

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with_hw_servers}
%pre Xorg
{
    pushd /etc/X11

    [ -e xorg.conf ] || return 0

    sed -i 's/^.*Load.*"(pex5|xie|xtt).*\n$"//gi' xorg.conf
    sed -i 's/^\s*Driver(.*)"keyboard"/Driver\1"kbd"/gi' xorg.conf
    sed -i 's/^.*Option.*"XkbRules".*"(xfree86|xorg)".*\n$//gi' xorg.conf
    sed -i 's#^\s*RgbPath.*$##gi' xorg.conf
    # lame, the nvidia driver needs to override this
    if ! grep -q 'ModulePath.*nvidia' xorg.conf ; then
      sed -i 's#^\s*ModulePath.*$##gi' xorg.conf
    fi

    popd
} &> /dev/null || :
%endif

%files common
%defattr(-,root,root,-)
%{_mandir}/man1/Xserver.1*
%{_libdir}/xorg/protocol.txt
%dir %{_localstatedir}/lib/xkb
%{_localstatedir}/lib/xkb/README.compiled


%if %{with_hw_servers}
%files Xorg
%defattr(-,root,root,-)
%{_bindir}/X
%attr(4711, root, root) %{_bindir}/Xorg
%{_bindir}/cvt
%{_bindir}/fedora-setup-keyboard
%{_bindir}/gtf
%dir %{_datadir}/xorg
%{_datadir}/hal/fdi/policy/10osvendor/10-x11-keymap.fdi
%{_datadir}/xorg/vesamodes
%{_datadir}/xorg/extramodes
%dir %{_libdir}/xorg
%dir %{_libdir}/xorg/modules
%dir %{_libdir}/xorg/modules/drivers
%dir %{_libdir}/xorg/modules/extensions
%{_libdir}/xorg/modules/extensions/libglx.so
%{_libdir}/xorg/modules/extensions/libdri.so
#{_libdir}/xorg/modules/extensions/libdri2.so
%{_libdir}/xorg/modules/extensions/libdbe.so
%{_libdir}/xorg/modules/extensions/libextmod.so
%dir %{_libdir}/xorg/modules/input
%dir %{_libdir}/xorg/modules/fonts
%{_libdir}/xorg/modules/fonts/libfreetype.so
%dir %{_libdir}/xorg/modules/linux
%{_libdir}/xorg/modules/linux/libfbdevhw.so
%dir %{_libdir}/xorg/modules/multimedia
%{_libdir}/xorg/modules/multimedia/bt829_drv.so
%{_libdir}/xorg/modules/multimedia/fi1236_drv.so
%{_libdir}/xorg/modules/multimedia/msp3430_drv.so
%{_libdir}/xorg/modules/multimedia/tda8425_drv.so
%{_libdir}/xorg/modules/multimedia/tda9850_drv.so
%{_libdir}/xorg/modules/multimedia/tda9885_drv.so
%{_libdir}/xorg/modules/multimedia/uda1380_drv.so
%{_libdir}/xorg/modules/libexa.so
%{_libdir}/xorg/modules/libfb.so
%{_libdir}/xorg/modules/libint10.so
%{_libdir}/xorg/modules/libshadow.so
%{_libdir}/xorg/modules/libshadowfb.so
%{_libdir}/xorg/modules/libvbe.so
%{_libdir}/xorg/modules/libvgahw.so
%{_libdir}/xorg/modules/libwfb.so
%{_libdir}/xorg/modules/libxaa.so
%{_libdir}/xorg/modules/libxf8_16bpp.so
%{_mandir}/man1/gtf.1*
%{_mandir}/man1/Xorg.1*
%{_mandir}/man1/cvt.1*
%{_mandir}/man4/fbdevhw.4*
%{_mandir}/man4/exa.4*
%{_mandir}/man5/xorg.conf.5*
%endif


%files Xnest
%defattr(-,root,root,-)
%{_bindir}/Xnest
%{_mandir}/man1/Xnest.1*


%files Xdmx
%defattr(-,root,root,-)
%{_bindir}/Xdmx
%{_bindir}/dmxaddinput
%{_bindir}/dmxaddscreen
%{_bindir}/dmxreconfig
%{_bindir}/dmxresize
%{_bindir}/dmxrminput
%{_bindir}/dmxrmscreen
%{_bindir}/dmxtodmx
%{_bindir}/dmxwininfo
%{_bindir}/vdltodmx
%{_bindir}/xdmx
%{_bindir}/xdmxconfig
%{_mandir}/man1/Xdmx.1*
%{_mandir}/man1/dmxtodmx.1*
%{_mandir}/man1/vdltodmx.1*
%{_mandir}/man1/xdmxconfig.1*


%files Xvfb
%defattr(-,root,root,-)
%{_bindir}/Xvfb
%{_bindir}/xvfb-run
%{_mandir}/man1/Xvfb.1*


%files Xephyr
%defattr(-,root,root,-)
%{_bindir}/Xephyr


%if %{with_hw_servers}
%files devel
%defattr(-,root,root,-)
%{_libdir}/libxf86config.a
%{_libdir}/pkgconfig/xorg-server.pc
%dir %{_includedir}/xorg
%{sdkdir}/*.h
%{_datadir}/aclocal/xorg-server.m4
%endif


%files source
%defattr(-, root, root, -)
%{xserver_source_dir}


%changelog
* Mon Oct 27 2008 Peter Hutterer <peter.hutterer@redhat.com> 1.5.2-9
- xserver-1.5.2-more-sanity-checks.patch: more sanity checks to stop vmmouse
  from segfaulting the server. #434807

* Wed Oct 22 2008 Peter Hutterer <peter.hutterer@redhat.com>
- Update xserver-1.5.2-disable-kbd-mouse.patch: add line to xorg.conf man-page
  stating that devices are disabled if AEI is on.

* Wed Oct 22 2008 Peter Hutterer <peter.hutterer@redhat.com>
- fix typo in xserver-1.5.2-no-duplicate-devices.patch

* Mon Oct 20 2008 Adam Jackson <ajax@redhat.com> 1.5.2-8
- xserver-1.5.2-exa-sync-less.patch: Avoid migrating pixmaps out on
  PutImage.

* Mon Oct 20 2008 Peter Hutterer <peter.hutterer@redhat.com> 1.5.2-7
- xserver-1.5.2-no-duplicate-devices.patch: don't re-add devices through HAL
  if they are already added (#467462).

* Sun Oct 19 2008 Peter Hutterer <peter.hutterer@redhat.com> 1.5.2-6
- Update xserver-1.5.2-disable-kbd-mouse.patch: if no config file is present,
  we need to force AllowEmptyInput on.

* Thu Oct 16 2008 Peter Hutterer <peter.hutterer@redhat.com> 1.5.2-5
- xserver-1.5.2-enable-RAW-console.patch: enable RAW mode for console, no need
  for grabbing the evdev device anymore.
- xserver-1.5.2-disable-kbd-mouse.patch: if AllowEmptyInput is on, don't allow
  mouse or keyboard drivers.

* Tue Oct 14 2008 Adam Jackson <ajax@redhat.com> 1.5.2-4
- xserver-1.5.2-lies-damn-lies-and-aspect-ratios.patch: Catch even more
  cases of the monitor encoding aspect ratio for size. (#458747)

* Tue Oct 14 2008 Adam Jackson <ajax@redhat.com> 1.5.2-3
- xserver-1.5.2-backtrace-defines.patch: Get HAVE_BACKTRACE defined even at
  the DIX level.

* Fri Oct 10 2008 Adam Jackson <ajax@redhat.com> 1.5.2-2
- xserver-1.5.1-global-backtrace.patch: Make backtraces possible from
  outside the xfree86 DDX.
- xserver-1.5.2-mieq-backtrace.patch: bt when we fill the input queue.

* Fri Oct 10 2008 Adam Jackson <ajax@redhat.com> 1.5.2-1
- xserver 1.5.2
- xserver-1.5.0-comment-out-glxdri2.c: Drop, no longer relevant.
- xserver-1.5.0-xkb-core-kbd-map-fix.patch: Drop, merged.
- xserver-1.5.1-int10-leaks.patch: Drop, merged.

* Fri Oct 10 2008 Adam Jackson <ajax@redhat.com> 1.5.1-11
- xserver-1.3.0-no-prerelease-warning.patch: Drop.

* Tue Oct 07 2008 Dave Airlie <airlied@redhat.com> 1.5.1-10
- actually apply exa fix patch

* Tue Oct 07 2008 Adam Jackson <ajax@redhat.com> 1.5.1-9
- xserver-1.5.1-xgi.patch: Move XGI cards onto the sis driver. (#453812)

* Tue Oct 07 2008 Adam Jackson <ajax@redhat.com> 1.5.1-8
- xserver-1.5.1-int10-leaks.patch: Shut up some useless int10 debugging and
  plug a memory leak.

* Tue Oct 7 2008 Adam Jackson <ajax@redhat.com> 1.5.1-7
- xserver-1.5.1-mode-debug.patch: Force mode debugging on.

* Tue Oct 7 2008 Peter Hutterer <peter.hutterer@redhat.com> 1.5.1-6
- xserver-1.5.0-xkb-core-kbd-map-fix.patch: don't invent groups when mapping
  from xkb to core and back, and squash canonical types into explicit ones on
  core reconstruction (2 patches). #460545

* Mon Oct 06 2008 Dave Airlie <airlied@redhat.com> 1.5.1-5
- xserver-1.5.1-exa-fix-glyph-segfault.patch - fix EXA rects crash (462447)

* Tue Sep 30 2008 Tom "spot" Callaway <tcallawa@redhat.com> 1.5.1-4
- fix typo. :P

* Tue Sep 30 2008 Tom "spot" Callaway <tcallawa@redhat.com> 1.5.1-3
- add xvfb-run helper script to Xvfb package

* Thu Sep 25 2008 Dave Airlie <airlied@redhat.com> 1.5.1-2
- fix crash with x11perf on r500 modesetting

* Tue Sep 23 2008 Adam Jackson <ajax@redhat.com> 1.5.1-1
- xserver 1.5.1
- Trim %%changelog.

* Thu Sep 11 2008 Soren Sandmann <sandmann@redhat.com> 1.5.0-6
- Comment out glxdri2.c since it doesn't compile. (krh says it
  won't break at runtime). 

* Thu Sep 11 2008 Soren Sandmann <sandmann@redhat.com> 1.5.0-5
- Bump BuildRequires on mesa-GL-devel. Maybe that will work.

* Thu Sep 11 2008 Soren Sandmann <sandmann@redhat.com> 1.5.0-4
- Bump BuildRequires on xorg-x11-proto-devel

* Thu Sep 11 2008 Soren Sandmann <sandmann@redhat.com> 1.5.0-3
- Change the external monitor patch to base off of amount of video ram.

* Thu Sep 11 2008 Soren Sandmann <sandmann@redhat.com> 1.5.0-3
- Change the default screen limits to include room for a 1280 wide
  projector.

* Wed Sep 10 2008 Dave Airlie <airlied@redhat.com> 1.5.0-2
- bring master exa back

* Wed Sep 03 2008 Adam Jackson <ajax@redhat.com> 1.5.0-1
- xserver 1.5.0
- Revert to the EXA from 1.5.0, should be good enough one hopes.
- Add .gitignore from git, so working with the artificial git tree is less
  flakey.

* Mon Aug 25 2008 Adam Jackson <ajax@redhat.com> 1.4.99.906-10
- xserver-1.5.0-edid-backport.patch: Backport EDID updates from master.

* Wed Aug 20 2008 Adam Jackson <ajax@redhat.com> 1.4.99.906-9
- xserver-1.5.0-hide-cursor.patch: Suppress displaying the cursor until
  an app calls XDefineCursor().

* Thu Aug 14 2008 Kristian Høgsberg <krh@redhat.com> - 1.4.99.906-8
- Add bg-none-root patch for plymouth.

* Thu Aug 14 2008 Dave Airlie <airlied@redhat.com> 1.4.99.906-7
- EXA backport master EXA code for optimisations

* Wed Aug 13 2008 Adam Jackson <ajax@redhat.com> 1.4.99.906-6
- xserver-1.5.0-enable-selinux.patch: Enable selinux again.

* Tue Aug 05 2008 Peter Hutterer <peter.hutterer@redhat.com> 1.4.99.906-5
- xserver-1.5.0-xkb-fix-ProcXkbSetXYZ-to-work-on-all.patch: force xkb requests
  to apply to all extension devices.
- drop call-SwitchCoreKeyboard.patch
- xserver-1.5.0-force-SwitchCoreKeyboard-for-evdev.patch: force
  SwitchCoreKeyboard for evdev devices to push device keymap into core device.

* Mon Aug 04 2008 Adam Jackson <ajax@redhat.com> 1.4.99.906-4
- 10-x11-keymap.fdi, fedora-setup-keyboard: Attempt to read keyboard settings
  from /etc/sysconfig/keyboard and stuff them into hal.

* Mon Aug 04 2008 Peter Hutterer <peter.hutterer@redhat.com> 1.4.99.906-3
- xserver-1.5.0-call-SwitchCoreKeyboard-for-first-device.patch: force a keymap
  switch to push the device keymap into the core device.

* Thu Jul 31 2008 Adam Jackson <ajax@redhat.com> 1.4.99.906-2
- Drop the evdev keyboarding patch.

* Thu Jul 24 2008 Adam Jackson <ajax@redhat.com> 1.4.99.906-1
- 1.5RC6.

* Wed Jul 02 2008 Adam Tkac <atkac redhat com> 1.4.99.905-2.20080701
- build with -rdynamic to make dri_swrast happy

* Mon Jun 30 2008 Adam Jackson <ajax@redhat.com> 1.4.99.905-1.20080701
- 1.5RC5.

* Thu Jun 19 2008 Adam Tkac <atkac redhat com>
- workaround broken AC_C_BIGENDIAN macro (#449944)

* Thu Jun 12 2008 Dave Airlie <airlied@redhat.com> 1.4.99.902-3.20080612
- xserver-1.5.0-fix-single-aspect.patch - fix 2560x1600 on my monitor.

* Thu Jun 12 2008 Dave Airlie <airlied@redhat.com> 1.4.99.902-2.20080612
- cve-2008-1377: Record and Security Extension Input validation
- cve-2008-1379: MIT-SHM extension Input Validation flaw
- cve-2008-2360: Render AllocateGlyph extension Integer overflows
- cve-2008-2361: Render CreateCursor extension Integer overflows
- cve-2008-2362: Render Gradient extension Integer overflows
- Rebase to 1.5 head for security patches for above

* Mon Jun 09 2008 Adam Jackson <ajax@redhat.com> 1.4.99.902-1.20080609
- Today's git snapshot.

* Tue May 06 2008 Bill Nottingham <notting@redhat.com> 1.4.99.901-29.20080415
- rebuild against new xorg-x11-xtrans-devel (#445303)

* Mon May 05 2008 Adam Jackson <ajax@redhat.com> 1.4.99.901-28.20080415
- xserver-1.5.0-compiz-clip-fix.patch: Make compiz stop blinking every
  so often. (#441219)

* Mon May 05 2008 Adam Jackson <ajax@redhat.com> 1.4.99.901-27.20080415
- xserver-1.5.0-hal-closedown.patch: Fix a crash in the hal code when
  closing a device.

* Mon Apr 28 2008 Soren Sandmann <sandmann@redhat.com>
- Preserve user's CFLAGS

* Thu Apr 24 2008 Adam Jackson <ajax@redhat.com> 1.4.99.901-26.20080415
- xserver-1.5.0-no-evdev-keyboards-kthnx.patch: Disable evdev for keyboards
  even on combo devices.  This means combo devices will go through the old
  mouse driver too.  Oh well.  (#440380)

* Thu Apr 24 2008 Dave Airlie <airlied@redhat.com> 1.4.99.901-25.20080415
- xserver-1.5.0-f-spot-screws-glx.patch: stop GLX crashing X server when
  f-spot exists (#443299)

* Wed Apr 23 2008 Dave Airlie <airlied@redhat.com> 1.4.99.901-24.20080415
- xserver-1.5.0-glcore-swap-no-crashy.patch: Fix issue with googleearth
  crashing GLcore.

* Tue Apr 22 2008 Adam Jackson <ajax@redhat.com> 1.4.99.901-23.20080415
- xserver-1.5.0-stenciled-visuals.patch: Prefer visuals with a stencil
  buffer for the default GLX visual.  (Hans de Goede, #442510)

* Tue Apr 15 2008 Dave Airlie <airlied@redhat.com> 1.4.99.901-22.20080415
- rebase to upstream server 1.5 branch from today - drop acr quirk

* Thu Apr 10 2008 Adam Jackson <ajax@redhat.com> 1.4.99.901-21.20080407
- xserver-1.5.0-selinux-off-by-default.patch: Re-disable selinux by default,
  again, in a way that lets you enable it if you really want to.

* Wed Apr 09 2008 Dave Airlie <airlied@redhat.com> 1.4.99.901-20.20080407
- xserver-1.5.0-quirk-acr.patch - add quirk for another monitor.

* Tue Apr 08 2008 Adam Jackson <ajax@redhat.com> 1.4.99.901-19.20080407
- Today's rebase.  Patch merge, some int10 fixes.

* Mon Apr 07 2008 Adam Jackson <ajax@redhat.com> 1.4.99.901-18.20080401
- xorg-x11-server-Red-Hat-extramodes.patch: Remove some of the more
  implausible modes.  Cargo cult programming woo.

* Fri Apr  4 2008 Kristian Høgsberg <krh@redhat.com> 1.4.99.901-17.20080401
- Add xserver-1.5.0-dont-bitch-about-record.patch (don't try to load
  librecord.so when we don't build it) and
  xserver-1.5.0-handle-failing-dri-create-screen.patch (#440491).

* Wed Apr  2 2008 Kristian Høgsberg <krh@redhat.com> 1.4.99.901-16.20080401
- Fix crash when DRI2 fails to initialize and crash when initializing
  software GL visuals (#440175).

* Tue Apr  1 2008 Kristian Høgsberg <krh@redhat.com> 1.4.99.901-15.20080401
- Rebase to new snapshot to pull in DRI2 direct rendering work.
- Stop shipping librecord.so.

* Tue Apr 01 2008 Adam Jackson <ajax@redhat.com> 1.4.99.901-14.20080314
- Remove vmmouse again, way too broken.  Let this be a lesson to you:
  never try.

* Thu Mar 27 2008 Adam Jackson <ajax@redhat.com> 1.4.99.901-13.20080314
- archify the vmmouse logic.

* Thu Mar 27 2008 Dave Airlie <airlied@redhat.com> 1.4.99.901-12.20080314
- xserver-1.5.0-fix-lsl-quirk.patch - fix the LSL quirk (#435216)

* Wed Mar 26 2008 Adam Jackson <ajax@redhat.com> 1.4.99.901-11.20080314
- xserver-1.5.0-vmmouse.patch: Use vmmouse(4) for the automagic mouse
  section.  It'll just fall back to the mouse(4) driver anyway if it's
  not a vmmouse.

* Tue Mar 18 2008 Adam Jackson <ajax@redhat.com> 1.4.99.901-10.20080314
- xserver-1.5.0-no-evdev-keyboards-kthnx.patch: Sorry, evdev keyboarding is
  just too broken.

* Fri Mar 14 2008 Adam Jackson <ajax@redhat.com> 1.4.99.901-9.20080314
- Today's snapshot.  Mostly just patch merge with rawhide.

* Thu Mar 13 2008 Adam Jackson <ajax@redhat.com> 1.4.99.901-8.20080310
- xserver-1.5.0-aspect-match.patch: Fix the RANDR 1.2 initial configuration
  heuristic for the case where the best possible mode is the first one in
  the first monitor's mode list.

* Thu Mar 13 2008 Adam Jackson <ajax@redhat.com> 1.4.99.901-7.20080310
- xserver-1.5.0-xaa-sucks: Disable XAA offscreen pixmaps by default.  They're
  almost always a performance loss anyway.  Use Option "XaaOffscreenPixmaps"
  to turn them back on.

* Thu Mar 13 2008 Dave Airlie <airlied@redhat.com> 1.4.99.901-6.20080310
- fix fbdev probing with no hardware to not load fbdev if pci slot claimed

* Wed Mar 12 2008 Adam Jackson <ajax@redhat.com> 1.4.99.901-5.20080310
- xserver-1.5.0-unselinux.patch: Disable selinux extension for now.
- xserver-1.5.0-ia64.patch: Fix ia64 PCI support. (#429878)

* Tue Mar 11 2008 Kristian Høgsberg <krh@redhat.com> 1.4.99.901-4.20080310
- Checkout the tip of the git snapshot so we get the most recent DRI2
  texture from pixmap changes in the build.  Bump mesa build requires.

* Tue Mar 11 2008 Adam Jackson <ajax@redhat.com> 1.4.99.901-3.20080310
- New 1.5 snapshot.
- xserver-1.5-x86emy.patch: Fix an x86emu quirk.

* Fri Mar 07 2008 Adam Jackson <ajax@redhat.com> 1.4.99.901-1.20080307
- Today's 1.5 snapshot.

* Tue Mar 04 2008 Adam Jackson <ajax@redhat.com> 1.4.99.900-0.28.20080304
- Today's 1.5 snapshot.
- Obsolete: xorg-x11-drv-magictouch to get it uninstalled.

* Mon Mar 03 2008 Adam Jackson <ajax@redhat.com> 1.4.99.900-0.27.20080303
- Switch to 1.5 branch and rebase.

* Thu Feb 28 2008 Jeremy Katz <katzj@redhat.com> - 1.4.99.1-0.26
- Pull in another SELinux fix from upstream

* Wed Feb 27 2008 Adam Jackson <ajax@redhat.com> 1.4.99.1-0.25
- Today's git snapshot.  Selinux fixes, XKB crash fix.

* Tue Feb 26 2008 Adam Jackson <ajax@redhat.com> 1.4.99.1-0.24
- Today's git snapshot.  PCI cleanups, AIGLX fix.

* Fri Feb 22 2008 Adam Jackson <ajax@redhat.com> 1.4.99.1-0.23
- Today's git snapshot.  Xinerama and XKB fixes, patch merging, etc.
- Remove some dead patches.

* Thu Feb 21 2008 Adam Jackson <ajax@redhat.com> 1.4.99.1-0.22
- Today's git snapshot, misc bugfixes.

* Fri Feb 15 2008 Adam Jackson <ajax@redhat.com> 1.4.99.1-0.21
- Today's git snapshot.  Features DRI2 and input hotplugging.  Tasty.

* Mon Feb 11 2008 Adam Jackson <ajax@redhat.com> 1.4.99.1-0.20
- Conflict against insufficiently new libpciaccess. (#390751)

* Tue Jan 29 2008 Adam Tkac <atkac redhat com> 1.4.99.1-0.19
- added dix/protocol.txt to source subpackage

* Fri Jan 18 2008 Dave Airlie <airlied@redhat.com> 1.4.99.1-0.18
- cve-2007-6429.patch: Fix patch to not break java apps

* Fri Jan 18 2008 Dave Airlie <airlied@redhat.com> 1.4.99.1-0.17
- cve-2007-5760.patch: XFree86-Misc Extension Invalid Array Index Vulnerability
- cve-2007-6427.patch: XInput Extension Memory Corruption Vulnerability
- cve-2007-6428.patch: TOG-CUP Extension Memory Corruption Vulnerability
- cve-2007-6429.patch: EVI and MIT-SHM Extension Integer Overflow Vulnerability
- cve-2008-0006-server-fixup.patch: PCF Font Vulnerability - this patch isn't strictly required with new version of libXfont.

* Wed Jan 16 2008 Kristian Høgsberg <krh@redhat.com> 1.4.99.1-0.16
- Add xserver-1.4.99-engage-composite-crack-mode.patch to better hide
  protocol side effects such as loss of grabs and focus when
  redirecting/unredirecting windows (#350271).

* Mon Jan 07 2008 Adam Jackson <ajax@redhat.com> 1.4.99.1-0.15
- Today's git snapshot.  X-SELinux!
- Drop the code to migrate from /etc/X11/XF86Config*.
- s/perl -p -i -e/sed -i/g

* Mon Jan 07 2008 Adam Jackson <ajax@redhat.com> 1.4.99.1-0.14
- Sync with F8 bugfixes:
  - xorg-x11-server-Red-Hat-extramodes.patch: Don't supply non-CVT-R timings
    for 1920x{1080,1200}.
  - xserver-1.3.0-ignore-extra-entity.patch: If a driver doesn't support
    secondary entities, don't fatal error just ignore and keep going.
  - xserver-1.3.0-randr-fix-set-rotations-xinerama.patch: Attempt to stop
    xinerama segfaulting randr12.

* Mon Dec 10 2007 Adam Jackson <ajax@redhat.com> 1.4.99.1-0.13
- xserver-1.4.99-alloca-poison.patch: Fatal error on {DE,}ALLOCATE_LOCAL
  so we don't build broken drivers.
- xserver-1.4.99-ssh-isnt-local.patch: Try harder to disable MIT-SHM for
  ssh-forwarded connections.

* Mon Dec 03 2007 Adam Jackson <ajax@redhat.com> 1.4.99.1-0.12
- xserver-1.4.99-apm-typedefs.patch: Temporary hack for broken kernels that
  don't publish the /dev/apm_bios types.

* Wed Nov 28 2007 Adam Jackson <ajax@redhat.com> 1.4.99.1-0.11
- Today's rebase.
- BR on git-core instead of git.
- Bump mesa-source BR to cope with extended CreatePixmap signature.
- xserver-1.4.99-openchrome.patch: Use openchrome not via when running
  without a config file.

* Tue Nov 13 2007 Adam Jackson <ajax@redhat.com> 1.4.99.1-0.10
- -devel Requires: pixman-devel and libpciaccess-devel.

* Mon Nov 12 2007 Adam Jackson <ajax@redhat.com> 1.4.99.1-0.8
- Fix buildrequires and other buildsystem nonsense.

* Fri Nov 02 2007 Adam Jackson <ajax@redhat.com> 1.4.99.1-0.6
- Merge a bunch of the more trivial patches upstream.
- New git snapshot containing the merged bits.
- Remove unused patches.
- Drop the XFree86 obsoletes.

* Fri Nov 02 2007 Adam Jackson <ajax@redhat.com> 1.4.99.1-0.5
- New git snapshot that fixes Xdmx build.
- Reenable Xdmx build.
- Rebase (or drop) the rest of our patches outside the PCI code.
- Add -common subpackage for shared files.
- Rename -sdk to -devel for verisimilitude.
- Simplify the %%configure line a bit.

* Thu Nov 01 2007 Adam Jackson <ajax@redhat.com> 1.4.99.1-0.4
- Update mesa and libdrm buildreqs.
- Reenable Xephyr build.

* Wed Oct 31 2007 Adam Jackson <ajax@redhat.com> 1.4.99.1-0.3
- Only invoke git-am once.
- Disable building mfb and cfb as well.

* Wed Oct 31 2007 Adam Jackson <ajax@redhat.com> 1.4.99.1-0.2
- BuildRequires: git.
- Manage the source directory as a git repo.
- Use git-am(1) to apply patches instead of %patch.
- Reformat a bunch of patches to conform to git-am's rules.
- Add wfb to file manifest.
- Drop afb, sorry Amiga users.
- Delete the SecurityPolicy man page from the buildroot, until we have a
  xorg-x11-server-common.
- Update to today's snapshot.

* Wed Oct 31 2007 Adam Jackson <ajax@redhat.com> 1.4.99.1-0.1
- Begin rebasing to git master.  It almost builds, assuming you disable
  glx, kdrive, and dmx, and remove like half the patches.
