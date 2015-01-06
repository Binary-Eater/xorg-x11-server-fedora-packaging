# This package is an experiment in active integration of upstream SCM with
# Fedora packaging.  It works something like this:
#
# The "pristine" source is actually a git repo (with no working checkout).
# The first step of %%prep is to check it out and switch to a "fedora" branch.
# If you need to add a patch to the server, just do it like a normal git
# operation, dump it with git-format-patch to a file in the standard naming
# format, and add a PatchN: line.  If you want to push something upstream,
# check out the master branch, pull, cherry-pick, and push.

#global gitdate 20140428
%global stable_abi 1

%if !0%{?gitdate} || %{stable_abi}
# Released ABI versions.  Have to keep these manually in sync with the
# source because rpm is a terrible language.
%global ansic_major 0
%global ansic_minor 4
%global videodrv_major 18
%global videodrv_minor 0
%global xinput_major 21
%global xinput_minor 0
%global extension_major 8
%global extension_minor 0
%endif

%if 0%{?gitdate}
# For git snapshots, use date for major and a serial number for minor
%global minor_serial 0
%global git_ansic_major %{gitdate}
%global git_ansic_minor %{minor_serial}
%global git_videodrv_major %{gitdate}
%global git_videodrv_minor %{minor_serial}
%global git_xinput_major %{gitdate}
%global git_xinput_minor %{minor_serial}
%global git_extension_major %{gitdate}
%global git_extension_minor %{minor_serial}
%endif

%global pkgname xorg-server

Summary:   X.Org X11 X server
Name:      xorg-x11-server
Version:   1.16.2.901
Release:   1%{?gitdate:.%{gitdate}}%{dist}
URL:       http://www.x.org
License:   MIT
Group:     User Interface/X

#VCS:      git:git://git.freedesktop.org/git/xorg/xserver
%if 0%{?gitdate}
# git snapshot.  to recreate, run:
# ./make-git-snapshot.sh `cat commitid`
Source0:   xorg-server-%{gitdate}.tar.xz
#Source0:   http://www.x.org/pub/individual/xserver/%{pkgname}-%{version}.tar.bz2
Source1:   make-git-snapshot.sh
Source2:   commitid
%else
Source0:   http://www.x.org/pub/individual/xserver/%{pkgname}-%{version}.tar.bz2
Source1:   gitignore
%endif

Source4:   10-quirks.conf

Source10:   xserver.pamd

# "useful" xvfb-run script
Source20:  http://svn.exactcode.de/t2/trunk/package/xorg/xorg-server/xvfb-run.sh

# for requires generation in drivers
Source30: xserver-sdk-abi-requires.release
Source31: xserver-sdk-abi-requires.git

# maintainer convenience script
Source40: driver-abi-rebuild.sh

# Trivial things to never merge upstream ever:
# This really could be done prettier.
Patch5002: xserver-1.4.99-ssh-isnt-local.patch

# ajax needs to upstream this
Patch6030: xserver-1.6.99-right-of.patch
#Patch6044: xserver-1.6.99-hush-prerelease-warning.patch

Patch7025: 0001-Always-install-vbe-and-int10-sdk-headers.patch

# do not upstream - do not even use here yet
Patch7027: xserver-autobind-hotplug.patch

# Fix multiple monitors in reverse optimus configurations
Patch8041: 0001-pixmap-fix-reverse-optimus-support-with-multiple-hea.patch

# submitted: http://lists.x.org/archives/xorg-devel/2013-October/037996.html
Patch9100: exa-only-draw-valid-trapezoids.patch

# because the display-managers are not ready yet, do not upstream
Patch10000: 0001-Fedora-hack-Make-the-suid-root-wrapper-always-start-.patch

# submitted http://lists.x.org/archives/xorg-devel/2014-July/042936.html
Patch10200: 0001-xwayland-Snap-damage-reports-to-the-bounding-box.patch

# already in master:
Patch10300: glamor-add-shm-sync-fence-support.patch
%global moduledir	%{_libdir}/xorg/modules
%global drimoduledir	%{_libdir}/dri
%global sdkdir		%{_includedir}/xorg

%ifarch s390 s390x
%global with_hw_servers 0
%else
%global with_hw_servers 1
%endif

%if %{with_hw_servers}
%global enable_xorg --enable-xorg
%else
%global enable_xorg --disable-xorg
%endif

%ifnarch %{ix86} x86_64
%global no_int10 --disable-vbe --disable-int10-module
%endif

%global kdrive --enable-kdrive --enable-xephyr --disable-xfake --disable-xfbdev
%global xservers --enable-xvfb --enable-xnest %{kdrive} %{enable_xorg}

BuildRequires: systemtap-sdt-devel
BuildRequires: git-core
BuildRequires: automake autoconf libtool pkgconfig
BuildRequires: xorg-x11-util-macros >= 1.17

BuildRequires: xorg-x11-proto-devel >= 7.7-10
BuildRequires: xorg-x11-font-utils >= 7.2-11

BuildRequires: dbus-devel libepoxy-devel systemd-devel
BuildRequires: xorg-x11-xtrans-devel >= 1.3.2
BuildRequires: libXfont-devel libXau-devel libxkbfile-devel libXres-devel
BuildRequires: libfontenc-devel libXtst-devel libXdmcp-devel
BuildRequires: libX11-devel libXext-devel
BuildRequires: libXinerama-devel libXi-devel

# DMX config utils buildreqs.
BuildRequires: libXt-devel libdmx-devel libXmu-devel libXrender-devel
BuildRequires: libXi-devel libXpm-devel libXaw-devel libXfixes-devel

%if 0%{?fedora} > 20
BuildRequires: wayland-devel
BuildRequires: pkgconfig(wayland-client) >= 1.3.0
BuildRequires: pkgconfig(epoxy)
%endif
%if !0%{?rhel}
BuildRequires: pkgconfig(xshmfence) >= 1.1
%endif
BuildRequires: libXv-devel
BuildRequires: pixman-devel >= 0.30.0
BuildRequires: libpciaccess-devel >= 0.13.1 openssl-devel byacc flex
BuildRequires: mesa-libGL-devel >= 9.2
BuildRequires: mesa-libEGL-devel
BuildRequires: mesa-libgbm-devel
# XXX silly...
BuildRequires: libdrm-devel >= 2.4.0 kernel-headers

BuildRequires: audit-libs-devel libselinux-devel >= 2.0.86-1
BuildRequires: libudev-devel
%if !0%{?rhel}
# libunwind is Exclusive for the following arches
%ifarch aarch64 %{arm} hppa ia64 mips ppc ppc64 %{ix86} x86_64
BuildRequires: libunwind-devel
%endif
%endif

BuildRequires: pkgconfig(xcb-aux) pkgconfig(xcb-image) pkgconfig(xcb-icccm)
BuildRequires: pkgconfig(xcb-keysyms)

# All server subpackages have a virtual provide for the name of the server
# they deliver.  The Xorg one is versioned, the others are intentionally
# unversioned.

%description
X.Org X11 X server


%package common
Summary: Xorg server common files
Group: User Interface/X
Requires: pixman >= 0.30.0
Requires: xkeyboard-config xkbcomp

%description common
Common files shared among all X servers.


%if %{with_hw_servers}
%package Xorg
Summary: Xorg X server
Group: User Interface/X
Provides: Xorg = %{version}-%{release}
Provides: Xserver
# HdG: This should be moved to the wrapper package once the wrapper gets
# its own sub-package:
Provides: xorg-x11-server-wrapper = %{version}-%{release}
%if !0%{?gitdate} || %{stable_abi}
Provides: xserver-abi(ansic-%{ansic_major}) = %{ansic_minor}
Provides: xserver-abi(videodrv-%{videodrv_major}) = %{videodrv_minor}
Provides: xserver-abi(xinput-%{xinput_major}) = %{xinput_minor}
Provides: xserver-abi(extension-%{extension_major}) = %{extension_minor}
%endif
%if 0%{?gitdate}
Provides: xserver-abi(ansic-%{git_ansic_major}) = %{git_ansic_minor}
Provides: xserver-abi(videodrv-%{git_videodrv_major}) = %{git_videodrv_minor}
Provides: xserver-abi(xinput-%{git_xinput_major}) = %{git_xinput_minor}
Provides: xserver-abi(extension-%{git_extension_major}) = %{git_extension_minor}
%endif
Obsoletes: xorg-x11-glamor < %{version}-%{release}
Provides: xorg-x11-glamor = %{version}-%{release}

%if 0%{?fedora} > 20
# Dropped from F21
Obsoletes: xorg-x11-drv-apm < 1.2.5-18
Obsoletes: xorg-x11-drv-cirrus < 1.5.2-10
Obsoletes: xorg-x11-drv-glint < 1.2.8-17
Obsoletes: xorg-x11-drv-i128 < 1.3.6-18
Obsoletes: xorg-x11-drv-i740 < 1.3.4-18
Obsoletes: xorg-x11-drv-mach64 < 6.9.4-16
Obsoletes: xorg-x11-drv-mga < 1.6.2-17
Obsoletes: xorg-x11-drv-neomagic < 1.2.8-8
Obsoletes: xorg-x11-drv-r128 < 6.9.1-15
Obsoletes: xorg-x11-drv-rendition < 4.2.5-18
Obsoletes: xorg-x11-drv-s3virge < 1.10.6-18
Obsoletes: xorg-x11-drv-savage < 2.3.7-7
Obsoletes: xorg-x11-drv-siliconmotion < 1.7.7-17
Obsoletes: xorg-x11-drv-sis < 0.10.7-19
Obsoletes: xorg-x11-drv-tdfx < 1.4.5-17
Obsoletes: xorg-x11-drv-trident < 1.3.6-18
%endif

Requires: xorg-x11-server-common >= %{version}-%{release}
Requires: system-setup-keyboard

%description Xorg
X.org X11 is an open source implementation of the X Window System.  It
provides the basic low level functionality which full fledged
graphical user interfaces (GUIs) such as GNOME and KDE are designed
upon.
%endif


%package Xnest
Summary: A nested server
Group: User Interface/X
Requires: xorg-x11-server-common >= %{version}-%{release}
Provides: Xnest

%description Xnest
Xnest is an X server which has been implemented as an ordinary
X application.  It runs in a window just like other X applications,
but it is an X server itself in which you can run other software.  It
is a very useful tool for developers who wish to test their
applications without running them on their real X server.


%package Xdmx
Summary: Distributed Multihead X Server and utilities
Group: User Interface/X
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
Summary: A X Windows System virtual framebuffer X server
Group: User Interface/X
# xvfb-run is GPLv2, rest is MIT
License: MIT and GPLv2
Requires: xorg-x11-server-common >= %{version}-%{release}
# required for xvfb-run
Requires: xorg-x11-xauth
Provides: Xvfb

%description Xvfb
Xvfb (X Virtual Frame Buffer) is an X server that is able to run on
machines with no display hardware and no physical input devices.
Xvfb simulates a dumb framebuffer using virtual memory.  Xvfb does
not open any devices, but behaves otherwise as an X display.  Xvfb
is normally used for testing servers.


%package Xephyr
Summary: A nested server
Group: User Interface/X
Requires: xorg-x11-server-common >= %{version}-%{release}
Provides: Xephyr

%description Xephyr
Xephyr is an X server which has been implemented as an ordinary
X application.  It runs in a window just like other X applications,
but it is an X server itself in which you can run other software.  It
is a very useful tool for developers who wish to test their
applications without running them on their real X server.  Unlike
Xnest, Xephyr renders to an X image rather than relaying the
X protocol, and therefore supports the newer X extensions like
Render and Composite.


%if 0%{?fedora} > 20
%package Xwayland
Summary: Wayland X Server
Group: User Interface/X
Requires: xorg-x11-server-common >= %{version}-%{release}

%description Xwayland
Xwayland is an X server for running X clients under Wayland.
%endif


%if %{with_hw_servers}
%package devel
Summary: SDK for X server driver module development
Group: User Interface/X
Requires: xorg-x11-util-macros
Requires: xorg-x11-proto-devel
Requires: pkgconfig pixman-devel libpciaccess-devel
Provides: xorg-x11-server-static
Obsoletes: xorg-x11-glamor-devel < %{version}-%{release}
Provides: xorg-x11-glamor-devel = %{version}-%{release}

%description devel
The SDK package provides the developmental files which are necessary for
developing X server driver modules, and for compiling driver modules
outside of the standard X11 source code tree.  Developers writing video
drivers, input drivers, or other X modules should install this package.
%endif


%package source
Summary: Xserver source code required to build VNC server (Xvnc)
Group: Development/Libraries
BuildArch: noarch

%description source
Xserver source code needed to build VNC server (Xvnc)


%prep
%setup -q -n %{pkgname}-%{?gitdate:%{gitdate}}%{!?gitdate:%{version}}
#setup -q -n %{pkgname}-%{version}

#if 0%{?gitdate}
%if 0
git checkout -b fedora
sed -i 's/git/&+ssh/' .git/config
if [ -z "$GIT_COMMITTER_NAME" ]; then
    git config user.email "x@fedoraproject.org"
    git config user.name "Fedora X Ninjas"
fi
%else
git init
if [ -z "$GIT_COMMITTER_NAME" ]; then
    git config user.email "x@fedoraproject.org"
    git config user.name "Fedora X Ninjas"
fi
cp %{SOURCE1} .gitignore
git add .
git commit -a -q -m "%{version} baseline."
%endif

# Apply all the patches.
git am -p1 %{patches} < /dev/null

%if %{with_hw_servers} && 0%{?stable_abi}
# check the ABI in the source against what we expect.
getmajor() {
    grep -i ^#define.ABI.$1_VERSION hw/xfree86/common/xf86Module.h |
    tr '(),' '   ' | awk '{ print $4 }'
}

getminor() {
    grep -i ^#define.ABI.$1_VERSION hw/xfree86/common/xf86Module.h |
    tr '(),' '   ' | awk '{ print $5 }'
}

test `getmajor ansic` == %{ansic_major}
test `getminor ansic` == %{ansic_minor}
test `getmajor videodrv` == %{videodrv_major}
test `getminor videodrv` == %{videodrv_minor}
test `getmajor xinput` == %{xinput_major}
test `getminor xinput` == %{xinput_minor}
test `getmajor extension` == %{extension_major}
test `getminor extension` == %{extension_minor}

%endif

%build

%global default_font_path "catalogue:/etc/X11/fontpath.d,built-ins"

%if %{with_hw_servers}
%global dri_flags --enable-dri2 %{?!rhel:--enable-dri3} --enable-suid-wrapper --enable-glamor
%else
%global dri_flags --disable-dri
%endif

%if 0%{?fedora}
%global bodhi_flags --with-vendor-name="Fedora Project"
%if 0%{?fedora} > 20
%global wayland --enable-xwayland
%else
%global wayland --disable-xwayland
%endif
%endif

# ick
%if 0%{?rhel}
sed -i 's/WAYLAND_SCANNER_RULES.*//g' configure.ac
%endif

# --with-pie ?
autoreconf -f -v --install || exit 1
# export CFLAGS="${RPM_OPT_FLAGS}"
# XXX without dtrace

%configure %{xservers} \
	--disable-static \
	--with-pic \
	%{?no_int10} --with-int10=x86emu \
	--with-default-font-path=%{default_font_path} \
	--with-module-dir=%{moduledir} \
	--with-builderstring="Build ID: %{name} %{version}-%{release}" \
	--with-os-name="$(hostname -s) $(uname -r)" \
	--with-xkb-output=%{_localstatedir}/lib/xkb \
        --without-dtrace \
	--disable-linux-acpi --disable-linux-apm \
	--enable-xselinux --enable-record --enable-present \
	--enable-config-udev \
	--disable-unit-tests \
	--enable-dmx \
	%{?wayland} \
	%{dri_flags} %{?bodhi_flags} \
	${CONFIGURE}
        
make V=1 %{?_smp_mflags}


%install
%make_install moduledir=%{moduledir}

%if %{with_hw_servers}
rm -rf $RPM_BUILD_ROOT%{_libdir}/xorg/modules/multimedia/
mkdir -p $RPM_BUILD_ROOT%{_libdir}/xorg/modules/{drivers,input}

mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/pam.d
install -m 644 %{SOURCE10} $RPM_BUILD_ROOT%{_sysconfdir}/pam.d/xserver

mkdir -p $RPM_BUILD_ROOT%{_datadir}/X11/xorg.conf.d
install -m 644 %{SOURCE4} $RPM_BUILD_ROOT%{_datadir}/X11/xorg.conf.d

# make sure the (empty) /etc/X11/xorg.conf.d is there, system-setup-keyboard
# relies on it more or less.
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/X11/xorg.conf.d

mkdir -p $RPM_BUILD_ROOT%{_bindir}

%if %{stable_abi}
install -m 755 %{SOURCE30} $RPM_BUILD_ROOT%{_bindir}/xserver-sdk-abi-requires
%else
sed -e s/@MAJOR@/%{gitdate}/g -e s/@MINOR@/%{minor_serial}/g %{SOURCE31} > \
    $RPM_BUILD_ROOT%{_bindir}/xserver-sdk-abi-requires
chmod 755 $RPM_BUILD_ROOT%{_bindir}/xserver-sdk-abi-requires
%endif

%endif

# Make the source package
%global xserver_source_dir %{_datadir}/xorg-x11-server-source
%global inst_srcdir %{buildroot}/%{xserver_source_dir}
mkdir -p %{inst_srcdir}/{Xext,xkb,GL,hw/{xquartz/bundle,xfree86/common}}
mkdir -p %{inst_srcdir}/{hw/dmx/doc,man,doc,hw/dmx/doxygen}
cp {,%{inst_srcdir}/}hw/xquartz/bundle/cpprules.in
cp {,%{inst_srcdir}/}man/Xserver.man
cp {,%{inst_srcdir}/}doc/smartsched
cp {,%{inst_srcdir}/}hw/dmx/doxygen/doxygen.conf.in
cp {,%{inst_srcdir}/}xserver.ent.in
cp {,%{inst_srcdir}/}hw/xfree86/Xorg.sh.in
cp xkb/README.compiled %{inst_srcdir}/xkb
cp hw/xfree86/xorgconf.cpp %{inst_srcdir}/hw/xfree86

install -m 0755 %{SOURCE20} $RPM_BUILD_ROOT%{_bindir}/xvfb-run

find . -type f | egrep '.*\.(c|h|am|ac|inc|m4|h.in|pc.in|man.pre|pl|txt)$' |
xargs tar cf - | (cd %{inst_srcdir} && tar xf -)
# SLEDGEHAMMER
find %{inst_srcdir}/hw/xfree86 -name \*.c -delete

# Remove unwanted files/dirs
{
    rm -f $RPM_BUILD_ROOT%{_libdir}/X11/Options
    rm -f $RPM_BUILD_ROOT%{_bindir}/in?
    rm -f $RPM_BUILD_ROOT%{_bindir}/ioport
    rm -f $RPM_BUILD_ROOT%{_bindir}/out?
    rm -f $RPM_BUILD_ROOT%{_bindir}/pcitweak
    rm -f $RPM_BUILD_ROOT%{_mandir}/man1/pcitweak.1*
    find $RPM_BUILD_ROOT -type f -name '*.la' | xargs rm -f -- || :
%if !%{with_hw_servers}
    rm -f $RPM_BUILD_ROOT%{_libdir}/pkgconfig/xorg-server.pc
    rm -f $RPM_BUILD_ROOT%{_datadir}/aclocal/xorg-server.m4
    rm -rf $RPM_BUILD_ROOT%{_defaultdocdir}/xorg-server
%endif
# wtf
%ifnarch %{ix86} x86_64
    rm -f $RPM_BUILD_ROOT%{_libdir}/xorg/modules/lib{int10,vbe}.so
%endif
}


%files common
%doc COPYING
%{_mandir}/man1/Xserver.1*
%{_libdir}/xorg/protocol.txt
%dir %{_localstatedir}/lib/xkb
%{_localstatedir}/lib/xkb/README.compiled

%if 1
%global Xorgperms %attr(4755, root, root)
%else
# disable until module loading is audited
%global Xorgperms %attr(0711,root,root) %caps(cap_sys_admin,cap_sys_rawio,cap_dac_override=pe)
%endif

%if %{with_hw_servers}
%files Xorg
%config %attr(0644,root,root) %{_sysconfdir}/pam.d/xserver
%{_bindir}/X
%{_bindir}/Xorg
%{_libexecdir}/Xorg.bin
%{Xorgperms} %{_libexecdir}/Xorg.wrap
%{_bindir}/cvt
%{_bindir}/gtf
%dir %{_libdir}/xorg
%dir %{_libdir}/xorg/modules
%dir %{_libdir}/xorg/modules/drivers
%dir %{_libdir}/xorg/modules/extensions
%{_libdir}/xorg/modules/extensions/libglx.so
%dir %{_libdir}/xorg/modules/input
%{_libdir}/xorg/modules/libfbdevhw.so
%{_libdir}/xorg/modules/libexa.so
%{_libdir}/xorg/modules/libfb.so
%{_libdir}/xorg/modules/libglamoregl.so
%{_libdir}/xorg/modules/libshadow.so
%{_libdir}/xorg/modules/libshadowfb.so
%{_libdir}/xorg/modules/libvgahw.so
%{_libdir}/xorg/modules/libwfb.so
%ifarch %{ix86} x86_64
%{_libdir}/xorg/modules/libint10.so
%{_libdir}/xorg/modules/libvbe.so
%endif
%{_mandir}/man1/gtf.1*
%{_mandir}/man1/Xorg.1*
%{_mandir}/man1/Xorg.wrap.1*
%{_mandir}/man1/cvt.1*
%{_mandir}/man4/fbdevhw.4*
%{_mandir}/man4/exa.4*
%{_mandir}/man5/Xwrapper.config.5*
%{_mandir}/man5/xorg.conf.5*
%{_mandir}/man5/xorg.conf.d.5*
%dir %{_sysconfdir}/X11/xorg.conf.d
%dir %{_datadir}/X11/xorg.conf.d
%{_datadir}/X11/xorg.conf.d/10-evdev.conf
%{_datadir}/X11/xorg.conf.d/10-quirks.conf
%endif


%files Xnest
%{_bindir}/Xnest
%{_mandir}/man1/Xnest.1*

%files Xdmx
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
%{_bindir}/dmxinfo
%{_bindir}/xdmxconfig
%{_mandir}/man1/Xdmx.1*
%{_mandir}/man1/dmxtodmx.1*
%{_mandir}/man1/vdltodmx.1*
%{_mandir}/man1/xdmxconfig.1*

%files Xvfb
%{_bindir}/Xvfb
%{_bindir}/xvfb-run
%{_mandir}/man1/Xvfb.1*

%files Xephyr
%{_bindir}/Xephyr
%{_mandir}/man1/Xephyr.1*

%if 0%{?fedora} > 20
%files Xwayland
%{_bindir}/Xwayland
%endif

%if %{with_hw_servers}
%files devel
%doc COPYING
#{_docdir}/xorg-server
%{_bindir}/xserver-sdk-abi-requires
%{_libdir}/pkgconfig/xorg-server.pc
%dir %{_includedir}/xorg
%{sdkdir}/*.h
%{_datadir}/aclocal/xorg-server.m4
%endif

%files source
%{xserver_source_dir}


%changelog
* Wed Dec 10 2014 Dave Airlie <airlied@redhat.com> 1.16.2.901-1
- upstream security release. 1.16.2.901

* Fri Nov 21 2014 Dave Airlie <airlied@redhat.com> 1.16.2-1
- New upstream bugfix release 1.16.2

* Fri Nov 21 2014 Dave Airlie <airlied@redhat.com> 1.16.1-2
- backport glamor DRI3 sync integration from upstream

* Fri Oct  3 2014 Hans de Goede <hdegoede@redhat.com> - 1.16.1-1
- New upstream bugfix release 1.16.1 (rhbz#1144404)

* Thu Sep 11 2014 Adam Jackson <ajax@redhat.com> 1.16.0-10
- Only send GLX_BufferSwapComplete for PresentCompleteKindPixmap

* Wed Sep 10 2014 Hans de Goede <hdegoede@redhat.com> - 1.16.0-9
- Fixup Xwayland summary, remove . at end of summaries (rhbz#1140225)

* Tue Sep 09 2014 Kalev Lember <kalevlember@gmail.com> - 1.16.0-8
- Update the versions of obsoletes for dropped drivers

* Tue Sep  2 2014 Hans de Goede <hdegoede@redhat.com> - 1.16.0-7
- Drop Fedora specific xorg-non-pci.patch, replace with solution from
  upstream

* Thu Aug 28 2014 Hans de Goede <hdegoede@redhat.com> - 1.16.0-6
- drop no longer valid configure arguments (rhbz#1133350)

* Mon Aug 25 2014 Peter Robinson <pbrobinson@fedoraproject.org> 1.16.0-5
- re-add support for non pci platform devices

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.16.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Aug  8 2014 Hans de Goede <hdegoede@redhat.com> - 1.16.0-3
- Really fix conditionals to allow building on F-20 (rhbz#1127351)

* Thu Aug  7 2014 Hans de Goede <hdegoede@redhat.com> - 1.16.0-2
- Fix xwayland conditionals to allow building on F-20 (rhbz#1127351)

* Mon Jul 28 2014 Hans de Goede <hdegoede@redhat.com> - 1.16.0-1
- Update to 1.16.0

* Thu Jul 17 2014 Adam Jackson <ajax@redhat.com> 1.15.99.904-4
- Add Obsoletes for video drivers dropped in F21+

* Fri Jul 11 2014 Hans de Goede <hdegoede@redhat.com> - 1.15.99.904-3
- Fix startx crash introduced by 1.15.99.904 (rhbz#1118540)

* Fri Jul 11 2014 Peter Hutterer <peter.hutterer@redhat.com> 1.15.99.904-2
- Don't force the screensaver off on DPMS unblank

* Tue Jul  8 2014 Hans de Goede <hdegoede@redhat.com> - 1.15.99.904-1
- Update to 1.15.99.904

* Wed Jul  2 2014 Hans de Goede <hdegoede@redhat.com> - 1.15.99.903-5
- Fix code including glamor.h not compiling due to strndup re-definition

* Wed Jul 02 2014 Adam Jackson <ajax@redhat.com> 1.15.99.903-4
- Snap xwayland damage reports to the bounding box

* Wed Jul  2 2014 Hans de Goede <hdegoede@redhat.com> - 1.15.99.903-3
- Fix xvfb crash on client disconnect (rhbz#1113128)

* Thu Jun 19 2014 Dennis Gilmore <dennis@ausil.us> - 1.15.99.903-2
- add support for non pci platform devices

* Wed Jun 11 2014 Hans de Goede <hdegoede@redhat.com> - 1.15.99.903-1
- Update to 1.15.99.903
- This bumps the videodrv ABI once more, so all drivers must be rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.15.99.902-8.20140428
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 21 2014 Adam Jackson <ajax@redhat.com> 1.15.99.902-7
- Don't try to build Xwayland in F20
- Fix shadowfb initialization to, er, work

* Wed May 14 2014 Peter Hutterer <peter.hutterer@redhat.com> - 1.15.99.902-6.20140428
- Revert button mapping for Evoluent Vertical mouse, the default mapping
  matches the manufacturer's documentation (#612140)

* Mon Apr 28 2014 Hans de Goede <hdegoede@redhat.com> - 1.15.99.902-5.20140428
- Add hw/xfree86/Xorg.sh.in to xorg-x11-server-source

* Mon Apr 28 2014 Hans de Goede <hdegoede@redhat.com> - 1.15.99.902-4.20140428
- Git snapshot 20140428
- This fixes the silent hardware cursor API break in 1.15.99.902 (#1090897)

* Fri Apr 25 2014 Hans de Goede <hdegoede@redhat.com> - 1.15.99.902-3
- Add missing BuildRequires for dbus-devel, libepoxy-devel, mesa-libEGL-devel,
  mesa-libgbm-devel and systemd-devel
- Fix compilation of int10 module on arm

* Wed Apr 23 2014 Hans de Goede <hdegoede@redhat.com> - 1.15.99.902-2
- Add --enable-glamor to configure flags

* Thu Apr 17 2014 Hans de Goede <hdegoede@redhat.com> - 1.15.99.902-1
- Update to 1.15.99.902
- Drop the Xwayland as extension patch-set
- Add a new xorg-x11-server-Xwayland package with the new standalone Xwayland
  server

* Fri Feb 28 2014 Peter Hutterer <peter.hutterer@redhat.com> 1.15.0-5
- Search all parent devices for a PnPID.

* Mon Feb 17 2014 Adam Williamson <awilliam@redhat.com> - 1.15.0-4
- fix xwayland crash under mutter (RH #1065109 , BGO #724443)

* Wed Feb 05 2014 Peter Hutterer <peter.hutterer@redhat.com> 1.15.0-3
- Prevent out-of-bounds access in check_butmap_change (#1061466)

* Tue Jan 14 2014 Adam Jackson <ajax@redhat.com> 1.15.0-2
- exa-only-draw-valid-trapezoids.patch: Fix crash in exa.

* Mon Jan 13 2014 Adam Jackson <ajax@redhat.com> 1.15.0-1
- xserver 1.15.0

* Tue Dec 17 2013 Adam Jackson <ajax@redhat.com> 1.14.99.904-1
- 1.15RC4
- Re-disable int10 on arm

* Mon Dec  2 2013 Peter Robinson <pbrobinson@fedoraproject.org> 1.14.99.902-2
- Add aarch64 to platforms that have libunwind

* Wed Nov 20 2013 Adam Jackson <ajax@redhat.com> 1.14.99.902-1
- 1.15RC2

* Mon Nov 18 2013 Adam Jackson <ajax@redhat.com> 1.14.99.901-6
- Prefer fbdev to vesa, fixes fallback path on UEFI

* Fri Nov 08 2013 Adam Jackson <ajax@redhat.com> 1.14.99.901-5
- Restore XkbCopyDeviceKeymap for (older) tigervnc

* Fri Nov 08 2013 Adam Jackson <ajax@redhat.com> 1.14.99.901-4
- Explicitly enable DRI2

* Thu Nov 07 2013 Adam Jackson <ajax@redhat.com> 1.14.99.901-3
- Merge Xinerama+{Damage,Render,Composite} fix series

* Thu Nov 07 2013 Adam Jackson <ajax@redhat.com> 1.14.99.901-2
- Fix build with --disable-present

* Thu Nov 07 2013 Adam Jackson <ajax@redhat.com
- Don't bother trying to build the unit tests for now

* Wed Nov 06 2013 Adam Jackson <ajax@redhat.com> 1.14.99.901-1
- 1.15RC1

* Mon Oct 28 2013 Adam Jackson <ajax@redhat.com> 1.14.99.3-2
- Don't build xwayland in RHEL

* Fri Oct 25 2013 Adam Jackson <ajax@redhat.com> 1.14.99.3-1
- xserver 1.14.99.3
- xwayland branch refresh
- Drop some F17-era Obsoletes
- Update BuildReqs to match reality

* Wed Oct 23 2013 Peter Hutterer <peter.hutterer@redhat.com> 1.14.3-6
- Fix Xdmx cursor jumps (#1019821)

* Tue Oct 08 2013 Adam Jackson <ajax@redhat.com> 1.14.3-5
- Snap wayland damage reports to the bounding box

* Thu Oct 03 2013 Adam Jackson <ajax@redhat.com> 1.14.3-4
- Fix up fixing up the driver list after filtering out non-wayland

* Wed Oct 02 2013 Adam Jackson <ajax@redhat.com> 1.14.3-3
- Only look at wayland-capable drivers when run with -wayland

* Mon Sep 23 2013 Adam Jackson <ajax@redhat.com> 1.14.3-2
- xwayland support

* Mon Sep 16 2013 Peter Hutterer <peter.hutterer@redhat.com> 1.14.3-1
- xserver 1.14.3

* Tue Jul 30 2013 Peter Hutterer <peter.hutterer@redhat.com> 1.14.2-9
- Fix active touch grabs, second touchpoint didn't get sent to client
- Fix version mismatch for XI 2.2+ clients (where a library supports > 2.2
  but another version than the originally requested one).

* Tue Jul 30 2013 Dave Airlie <airlied@redhat.com> 1.14.2-8
- fixes for multi-monitor reverse optimus

* Mon Jul 22 2013 Peter Hutterer <peter.hutterer@redhat.com> 1.14.2-7
- Fix erroneous valuator 1 coordinate when an absolute device in relative
  mode doesn't send y coordinates.

* Fri Jul 19 2013 Peter Hutterer <peter.hutterer@redhat.com> 1.14.2-6
- Add new version of the resolution-based scaling patch - scale y down
  instead of x up. That gives almost the same behaviour as current
  synaptics. Drop the synaptics quirk, this needs to be now removed from the
  driver.

* Mon Jul 15 2013 Peter Hutterer <peter.hutterer@redhat.com> 1.14.2-5
- Fix logspam when trying to free a non-existant grab.
- Update touch patch to upstream version (from fdo #66720)
- re-add xephyr resizable patch, got lost in rebase (#976995)

* Fri Jul 12 2013 Dave Airlie <airlied@redhat.com> 1.14.2-4
- reapply dropped patch to fix regression (#981953)

* Tue Jul 09 2013 Peter Hutterer <peter.hutterer@redhat.com> 1.14.2-3
- Fix crash on 32-bit with virtual box guest additions (#972095)

* Tue Jul 09 2013 Peter Hutterer <peter.hutterer@redhat.com> 1.14.2-2
- Fix crash in gnome-shell when tapping a menu twice (fdo #66720)

* Thu Jul 04 2013 Peter Hutterer <peter.hutterer@redhat.com> 1.14.2-1
- xorg-server 1.4.2
- drop merged patches
- Add a quirk to set the synaptics resolution to 0 by default. The pre-scale
  patch in the server clashes with synaptics inaccurate resolution numbers,
  causing the touchpad movement to be stunted.

* Thu Jun 06 2013 Peter Hutterer <peter.hutterer@redhat.com> 1.14.1.901-2
- Backport the touch grab race condition patches from fdo #56578

* Thu Jun 06 2013 Peter Hutterer <peter.hutterer@redhat.com> 1.14.1.901-1
- xserver 1.14.2RC1

* Tue Jun 04 2013 Peter Hutterer <peter.hutterer@redhat.com> 1.14.1-4
- Update quirks for trackballs and the La-VIEW Technology Naos 5000 mouse
