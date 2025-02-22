# This package is an experiment in active integration of upstream SCM with
# Fedora packaging.  It works something like this:
#
# The "pristine" source is actually a git repo (with no working checkout).
# The first step of %%prep is to check it out and switch to a "fedora" branch.
# If you need to add a patch to the server, just do it like a normal git
# operation, dump it with git-format-patch to a file in the standard naming
# format, and add a PatchN: line.  If you want to push something upstream,
# check out the master branch, pull, cherry-pick, and push.

# X.org requires lazy relocations to work.
%undefine _hardened_build
%undefine _strict_symbol_defs_build

#global gitdate 20161026
%global stable_abi 1

%if !0%{?gitdate} || %{stable_abi}
# Released ABI versions.  Have to keep these manually in sync with the
# source because rpm is a terrible language.
%global ansic_major 0
%global ansic_minor 4
%global videodrv_major 24
%global videodrv_minor 1
%global xinput_major 24
%global xinput_minor 1
%global extension_major 10
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
Version:   1.20.14
Release:   37%{?gitdate:.%{gitdate}}%{?dist}
URL:       http://www.x.org
# SPDX
License:   Adobe-Display-PostScript AND BSD-3-Clause AND DEC-3-Clause AND HPND AND HPND-sell-MIT-disclaimer-xserver AND HPND-sell-variant AND ICU AND ISC AND MIT AND MIT-open-group AND NTP AND SGI-B-2.0 AND SMLNJ AND X11 AND X11-distribute-modifications-variant

#VCS:      git:git://git.freedesktop.org/git/xorg/xserver
%if 0%{?gitdate}
# git snapshot.  to recreate, run:
# ./make-git-snapshot.sh `cat commitid`
Source0:   xorg-server-%{gitdate}.tar.xz
#Source0:   http://www.x.org/pub/individual/xserver/%{pkgname}-%{version}.tar.bz2
Source1:   make-git-snapshot.sh
Source2:   commitid
%else
Source0:   https://www.x.org/pub/individual/xserver/%{pkgname}-%{version}.tar.xz
Source1:   gitignore
%endif

Source10:   xserver.pamd

# "useful" xvfb-run script
Source20:  http://svn.exactcode.de/t2/trunk/package/xorg/xorg-server/xvfb-run.sh

# for requires generation in drivers
Source30: xserver-sdk-abi-requires.release
Source31: xserver-sdk-abi-requires.git

# maintainer convenience script
Source40: driver-abi-rebuild.sh

# From Debian use intel ddx driver only for gen4 and older chipsets
Patch1: 06_use-intel-only-on-pre-gen4.diff
# Default to xf86-video-modesetting on GeForce 8 and newer
Patch2: 0001-xfree86-use-modesetting-driver-by-default-on-GeForce.patch

# Default to va_gl on intel i965 as we use the modesetting drv there
# va_gl should probably just be the default everywhere ?
Patch3: 0001-xf86-dri2-Use-va_gl-as-vdpau_driver-for-Intel-i965-G.patch

# Submitted upstream, but not going anywhere
Patch5: 0001-autobind-GPUs-to-the-screen.patch

# because the display-managers are not ready yet, do not upstream
Patch6: 0001-Fedora-hack-Make-the-suid-root-wrapper-always-start-.patch

# Not sure anyone else cares about this so let's keep this Fedora-only for now
# Upstream PR for the meson.build equivalent is here, so we can drop this patch
# when we start building with meson.
# https://gitlab.freedesktop.org/xorg/xserver/-/merge_requests/1001`
Patch7: 0001-configure.ac-search-for-the-fontrootdir-ourselves.patch

# Backports from current stable "server-1.20-branch":
# <empty>

# Backports from "master" upstream:
Patch100: 0001-present-Check-for-NULL-to-prevent-crash.patch
Patch101: 0001-render-Fix-build-with-gcc-12.patch
Patch102: 0001-xf86-Accept-devices-with-the-simpledrm-driver.patch
Patch103: 0001-Don-t-hardcode-fps-for-fake-screen.patch
Patch104: 0001-hw-Rename-boolean-config-value-field-from-bool-to-bo.patch
Patch105: 0001-add-a-quirk-for-apple-silicon.patch
Patch106: 0001-xquartz-Remove-invalid-Unicode-sequence.patch

# CVE-2022-2319/ZDI-CAN-16062, CVE-2022-2320/ZDI-CAN-16070
Patch110: 0001-xkb-switch-to-array-index-loops-to-moving-pointers.patch
Patch111: 0002-xkb-swap-XkbSetDeviceInfo-and-XkbSetDeviceInfoCheck.patch
Patch112: 0003-xkb-add-request-length-validation-for-XkbSetGeometry.patch

# CVE-2022-3550
Patch113: 0001-xkb-proof-GetCountedString-against-request-length-at.patch
# CVE-2022-3551
Patch114: 0001-xkb-fix-some-possible-memleaks-in-XkbGetKbdByName.patch

# CVE-2022-46340
Patch115: 0001-Xtest-disallow-GenericEvents-in-XTestSwapFakeInput.patch
# related to CVE-2022-46344
Patch116: 0002-Xi-return-an-error-from-XI-property-changes-if-verif.patch
# CVE-2022-46344
Patch117: 0003-Xi-avoid-integer-truncation-in-length-check-of-ProcX.patch
# CVE-2022-46341
Patch118: 0004-Xi-disallow-passive-grabs-with-a-detail-255.patch
# CVE-2022-46343
Patch119: 0005-Xext-free-the-screen-saver-resource-when-replacing-i.patch
# CVE-2022-46342
Patch120: 0006-Xext-free-the-XvRTVideoNotify-when-turning-off-from-.patch
# CVE-2022-46283
Patch121: 0007-xkb-reset-the-radio_groups-pointer-to-NULL-after-fre.patch
# Fix for buggy patch to CVE-2022-46340
Patch122: 0008-Xext-fix-invalid-event-type-mask-in-XTestSwapFakeInp.patch
# CVE-2023-0494
Patch123: 0001-Xi-fix-potential-use-after-free-in-DeepCopyPointerCl.patch
# CVE-2023-1393
Patch124: 0001-composite-Fix-use-after-free-of-the-COW.patch
# https://gitlab.freedesktop.org/xorg/xserver/-/merge_requests/1114
Patch125: xorg-x11-server-fb-access-wrapper.patch
# https://gitlab.freedesktop.org/xorg/xserver/-/merge_requests/1057
Patch126: 0001-present-Send-a-PresentConfigureNotify-event-for-dest.patch

# CVE-2023-5367
Patch1010: 0001-Xi-randr-fix-handling-of-PropModeAppend-Prepend.patch
# CVE-2023-5380
Patch1011: 0002-mi-reset-the-PointerWindows-reference-on-screen-swit.patch
# CVE-2023-6377
Patch1012: 0001-Xi-allocate-enough-XkbActions-for-our-buttons.patch
# CVE-2023-6478
Patch1013: 0001-randr-avoid-integer-truncation-in-length-check-of-Pr.patch
# CVE-2023-6816
Patch1014: 0001-dix-allocate-enough-space-for-logical-button-maps.patch
# CVE-2024-0229
Patch1015: 0002-dix-Allocate-sufficient-xEvents-for-our-DeviceStateN.patch
Patch1016: 0003-dix-fix-DeviceStateNotify-event-calculation.patch
Patch1017: 0004-Xi-when-creating-a-new-ButtonClass-set-the-number-of.patch
# CVE-2024-21885
Patch1018: 0005-Xi-flush-hierarchy-events-after-adding-removing-mast.patch
# CVE-2024-21886
Patch1019: 0006-Xi-do-not-keep-linked-list-pointer-during-recursion.patch
Patch1020: 0007-dix-when-disabling-a-master-float-disabled-slaved-de.patch
# CVE-2024-0408
Patch1021: 0008-glx-Call-XACE-hooks-on-the-GLX-buffer.patch
# CVE-2024-0409
Patch1022: 0009-ephyr-xwayland-Use-the-proper-private-key-for-cursor.patch
# Related to CVE-2024-21886
Patch1023: 0001-dix-Fix-use-after-free-in-input-device-shutdown.patch
# Fix compilation error on i686
Patch1024: 0001-ephyr-Fix-incompatible-pointer-type-build-error.patch
# Fix copy and paste error in CVE-2024-0229
Patch1025: 0001-dix-fix-valuator-copy-paste-error-in-the-DeviceState.patch
# CVE-2024-31080
Patch1026: 0001-Xi-ProcXIGetSelectedEvents-needs-to-use-unswapped-le.patch
# CVE-2024-31081
Patch1027: 0002-Xi-ProcXIPassiveGrabDevice-needs-to-use-unswapped-le.patch
# CVE-2024-31082
Patch1028: 0003-Xquartz-ProcAppleDRICreatePixmap-needs-to-use-unswap.patch
# CVE-2024-31083
Patch1029: 0004-render-fix-refcounting-of-glyphs-during-ProcRenderAd.patch
Patch1030: 0001-render-Avoid-possible-double-free-in-ProcRenderAddGl.patch

## Add new patches above; Fedora-specific patches below

# Only on F38 and later (patch number starts at 3801, see autopatch below)
# Upstream commits 73d6e88, f69280dd and 4127776, minus the xwayland.pc.in change
Patch3801: 0001-Disallow-byte-swapped-clients-by-default.patch

BuildRequires: make
BuildRequires: systemtap-sdt-devel
BuildRequires: git-core
BuildRequires: automake autoconf libtool pkgconfig
BuildRequires: xorg-x11-util-macros >= 1.17

BuildRequires: xorg-x11-proto-devel >= 7.7-10

BuildRequires: dbus-devel libepoxy-devel systemd-devel
BuildRequires: xorg-x11-xtrans-devel >= 1.3.2
BuildRequires: libXfont2-devel libXau-devel libxkbfile-devel libXres-devel
BuildRequires: libfontenc-devel libXtst-devel libXdmcp-devel
BuildRequires: libX11-devel libXext-devel
BuildRequires: libXinerama-devel libXi-devel

# DMX config utils buildreqs.
BuildRequires: libXt-devel libdmx-devel libXmu-devel libXrender-devel
BuildRequires: libXi-devel libXpm-devel libXaw-devel libXfixes-devel

BuildRequires: pkgconfig(epoxy)
BuildRequires: pkgconfig(xshmfence) >= 1.1
BuildRequires: libXv-devel
BuildRequires: pixman-devel >= 0.30.0
BuildRequires: libpciaccess-devel >= 0.13.1 openssl-devel bison flex
BuildRequires: mesa-libGL-devel >= 9.2
BuildRequires: mesa-libEGL-devel
BuildRequires: mesa-libgbm-devel
# XXX silly...
BuildRequires: libdrm-devel >= 2.4.0 kernel-headers

BuildRequires: audit-libs-devel libselinux-devel >= 2.0.86-1
BuildRequires: libudev-devel
# libunwind is Exclusive for the following arches
%ifarch aarch64 %{arm} hppa ia64 mips ppc ppc64 %{ix86} x86_64
%if !0%{?rhel}
BuildRequires: libunwind-devel
%endif
%endif

BuildRequires: pkgconfig(xcb-aux) pkgconfig(xcb-image) pkgconfig(xcb-icccm)
BuildRequires: pkgconfig(xcb-keysyms) pkgconfig(xcb-renderutil)

%description
X.Org X11 X server


%package common
Summary: Xorg server common files
Requires: pixman >= 0.30.0
Requires: xkeyboard-config xkbcomp

%description common
Common files shared among all X servers.


%package Xorg
Summary: Xorg X server
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
Obsoletes: xorg-x11-drv-modesetting < %{version}-%{release}
Provides: xorg-x11-drv-modesetting = %{version}-%{release}
# Dropped from F25
Obsoletes: xorg-x11-drv-vmmouse < 13.1.0-4

Requires: xorg-x11-server-common >= %{version}-%{release}
Requires: system-setup-keyboard
Requires: xorg-x11-drv-libinput
Requires: libEGL

%description Xorg
X.org X11 is an open source implementation of the X Window System.  It
provides the basic low level functionality which full fledged
graphical user interfaces (GUIs) such as GNOME and KDE are designed
upon.


%package Xnest
Summary: A nested server
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
# xvfb-run is GPLv2, rest is MIT
License: MIT and GPLv2
Requires: xorg-x11-server-common >= %{version}-%{release}
# required for xvfb-run
Requires: xorg-x11-xauth
Requires: util-linux
Provides: Xvfb

%description Xvfb
Xvfb (X Virtual Frame Buffer) is an X server that is able to run on
machines with no display hardware and no physical input devices.
Xvfb simulates a dumb framebuffer using virtual memory.  Xvfb does
not open any devices, but behaves otherwise as an X display.  Xvfb
is normally used for testing servers.


%package Xephyr
Summary: A nested server
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


%package devel
Summary: SDK for X server driver module development
Requires: xorg-x11-util-macros
Requires: xorg-x11-proto-devel
Requires: libXfont2-devel
Requires: pkgconfig pixman-devel libpciaccess-devel
Provides: xorg-x11-server-static
Obsoletes: xorg-x11-glamor-devel < %{version}-%{release}
Provides: xorg-x11-glamor-devel = %{version}-%{release}

%description devel
The SDK package provides the developmental files which are necessary for
developing X server driver modules, and for compiling driver modules
outside of the standard X11 source code tree.  Developers writing video
drivers, input drivers, or other X modules should install this package.


%package source
Summary: Xserver source code required to build VNC server (Xvnc)
BuildArch: noarch

%description source
Xserver source code needed to build VNC server (Xvnc)


%prep
%autosetup -N -n %{pkgname}-%{?gitdate:%{gitdate}}%{!?gitdate:%{version}}
rm -rf .git
cp %{SOURCE1} .gitignore
# ick
%global __scm git
%{expand:%__scm_setup_git -q}
%if 0%{?fedora} >= 38
%autopatch
%else
%autopatch -M 3800
%endif

%if 0%{?stable_abi}
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

export CFLAGS="$RPM_OPT_FLAGS -specs=/usr/lib/rpm/redhat/redhat-hardened-cc1"
export CXXFLAGS="$RPM_OPT_FLAGS -specs=/usr/lib/rpm/redhat/redhat-hardened-cc1"
export LDFLAGS="$RPM_LD_FLAGS -specs=/usr/lib/rpm/redhat/redhat-hardened-ld"

%if !0%{?rhel}
%ifarch %{ix86} x86_64
%global int10_arch 1
%endif
%endif

%if %{undefined int10_arch}
%global no_int10 --disable-vbe --disable-int10-module
%endif

%global kdrive --enable-kdrive --enable-xephyr --disable-xfake --disable-xfbdev
%global xservers --enable-xvfb --enable-xnest %{kdrive} --enable-xorg
%global default_font_path "catalogue:/etc/X11/fontpath.d,built-ins"
%global dri_flags --disable-dri --enable-dri2 %{?!rhel:--enable-dri3} --enable-suid-wrapper --enable-glamor

autoreconf -f -v --install || exit 1

%configure %{xservers} \
	--enable-dependency-tracking \
	--disable-static \
	--with-pic \
	%{?no_int10} \
	--with-default-font-path=%{default_font_path} \
	--with-module-dir=%{_libdir}/xorg/modules \
	--with-builderstring="Build ID: %{name} %{version}-%{release}" \
	--with-os-name="$(hostname -s) $(uname -r)" \
	--with-xkb-output=%{_localstatedir}/lib/xkb \
        --without-dtrace \
	--disable-linux-acpi --disable-linux-apm \
	--enable-xselinux --enable-record --enable-present \
        --enable-xcsecurity \
	--enable-config-udev \
	--disable-unit-tests \
	--enable-dmx \
	--disable-xwayland \
	%{dri_flags} \
	${CONFIGURE}

make V=1 %{?_smp_mflags}


%install
%make_install

mkdir -p $RPM_BUILD_ROOT%{_libdir}/xorg/modules/{drivers,input}

mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/pam.d
install -m 644 %{SOURCE10} $RPM_BUILD_ROOT%{_sysconfdir}/pam.d/xserver

# make sure the (empty) /etc/X11/xorg.conf.d is there, system-setup-keyboard
# relies on it more or less.
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/X11/xorg.conf.d

%if %{stable_abi}
install -m 755 %{SOURCE30} $RPM_BUILD_ROOT%{_bindir}/xserver-sdk-abi-requires
%else
sed -e s/@MAJOR@/%{gitdate}/g -e s/@MINOR@/%{minor_serial}/g %{SOURCE31} > \
    $RPM_BUILD_ROOT%{_bindir}/xserver-sdk-abi-requires
chmod 755 $RPM_BUILD_ROOT%{_bindir}/xserver-sdk-abi-requires
%endif

install -m 0755 %{SOURCE20} $RPM_BUILD_ROOT%{_bindir}/xvfb-run

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

find . -type f | egrep '.*\.(c|h|am|ac|inc|m4|h.in|pc.in|man.pre|pl|txt)$' |
xargs tar cf - | (cd %{inst_srcdir} && tar xf -)
find %{inst_srcdir}/hw/xfree86 -name \*.c -delete

# Remove unwanted files/dirs
{
    find $RPM_BUILD_ROOT -type f -name '*.la' | xargs rm -f -- || :
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

%files Xorg
%config %attr(0644,root,root) %{_sysconfdir}/pam.d/xserver
%{_bindir}/X
%{_bindir}/Xorg
%{_libexecdir}/Xorg
%{Xorgperms} %{_libexecdir}/Xorg.wrap
%{_bindir}/cvt
%{_bindir}/gtf
%dir %{_libdir}/xorg
%dir %{_libdir}/xorg/modules
%dir %{_libdir}/xorg/modules/drivers
%{_libdir}/xorg/modules/drivers/modesetting_drv.so
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
%if %{defined int10_arch}
%{_libdir}/xorg/modules/libint10.so
%{_libdir}/xorg/modules/libvbe.so
%endif
%{_mandir}/man1/gtf.1*
%{_mandir}/man1/Xorg.1*
%{_mandir}/man1/Xorg.wrap.1*
%{_mandir}/man1/cvt.1*
%{_mandir}/man4/fbdevhw.4*
%{_mandir}/man4/exa.4*
%{_mandir}/man4/modesetting.4*
%{_mandir}/man5/Xwrapper.config.5*
%{_mandir}/man5/xorg.conf.5*
%{_mandir}/man5/xorg.conf.d.5*
%dir %{_sysconfdir}/X11/xorg.conf.d
%dir %{_datadir}/X11/xorg.conf.d
%{_datadir}/X11/xorg.conf.d/10-quirks.conf

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

%files devel
%doc COPYING
#{_docdir}/xorg-server
%{_bindir}/xserver-sdk-abi-requires
%{_libdir}/pkgconfig/xorg-server.pc
%dir %{_includedir}/xorg
%{_includedir}/xorg/*.h
%{_datadir}/aclocal/xorg-server.m4

%files source
%{xserver_source_dir}


%changelog
* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.20.14-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Apr 10 2024 José Expósito <jexposit@redhat.com> - 1.20.14-35
- Backport fix for invalid Unicode sequence

* Wed Apr 10 2024 José Expósito <jexposit@redhat.com> - 1.20.14-35
- Fix regression caused by the fix for CVE-2024-31083

* Wed Apr 03 2024 José Expósito <jexposit@redhat.com> - 1.20.14-34
- CVE fix for: CVE-2024-31080, CVE-2024-31081, CVE-2024-31082 and
  CVE-2024-31083

* Mon Mar 04 2024 José Expósito <jexposit@redhat.com> - 1.20.14-33
- Add util-linux as a dependency of Xvfb

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.20.14-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 José Expósito <jexposit@redhat.com> - 1.20.14-31
- Fix compilation error on i686

* Fri Jan 19 2024 José Expósito <jexposit@redhat.com> - 1.20.14-30
- Fix use after free related to CVE-2024-21886

* Tue Jan 16 2024 José Expósito <jexposit@redhat.com> - 1.20.14-29
- CVE fix for: CVE-2023-6816, CVE-2024-0229, CVE-2024-21885, CVE-2024-21886,
  CVE-2024-0408 and CVE-2024-0409

* Wed Dec 13 2023 Peter Hutterer <peter.hutterer@redhat.com> - 1.20.14-28
- CVE fix for: CVE-2023-6377, CVE-2023-6478

* Fri Nov 10 2023 Peter Hutterer <peter.hutterer@redhat.com> - 1.20.14-27
- Update with full SPDX license list

* Wed Oct 25 2023 Peter Hutterer <peter.hutterer@redhat.com> - 1.20.14-26
- CVE fix for: CVE-2023-5367, CVE-2023-5380

* Fri Oct 20 2023 José Expósito <jexposit@redhat.com>
- SPDX migration: license is already SPDX compatible

* Fri Sep 29 2023 Orion Poplawski <orion@nwra.com> - 1.20.14-25
- Fix xvfb-run --error-file / auth-file options

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.20.14-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Apr 25 2023 Olivier Fourdan <ofourdan@redhat.com> - 1.20.14-23
- Backport fix for a deadlock with DRI3 (#2189434)

* Thu Apr 13 2023 Florian Weimer <fweimer@redhat.com> - 1.20.14-22
- Make more functions available in fb.h with !FB_ACCESS_WRAPPER

* Wed Mar 29 2023 Olivier Fourdan <ofourdan@redhat.com> - 1.20.14-21
- CVE fix for: CVE-2023-1393

* Thu Feb 23 2023 Olivier Fourdan <ofourdan@redhat.com> - 1.20.14-20
- Fix xvfb-run script with --listen-tcp

* Thu Feb 09 2023 Iker Pedrosa <ipedrosa@redhat.com> - 1.20.14-19
- Remove pam_console from service file (#1822209)

* Thu Feb 02 2023 Peter Hutterer <peter.hutterer@redhat.com> - 1.20.14-18
- CVE-2023-0494: potential use-after-free

* Wed Feb 01 2023 Peter Hutterer <peter.hutterer@redhat.com> - 1.20.14-17
- Updated conditional fedora statement

* Tue Jan 17 2023 Olivier Fourdan <ofourdan@redhat.com> - 1.20.14-16
- Use the recommended way to apply conditional patches without
  conditionalizing the sources (for byte-swapped clients).

* Fri Jan 13 2023 Leif Liddy <leifliddy@fedoraproject.org> 1.20.14-15
- Xorg server does not correctly select the DCP for the display
  without a quirk on Apple silicon machines (#2152414)

* Fri Jan 13 2023 Peter Hutterer <peter.hutterer@redhat.com> - 1.20.14-14
- Disallow byte-swapped clients (#2159489)

* Wed Jan 11 2023 Olivier Fourdan <ofourdan@redhat.com> - 1.20.14-13
- Rename boolean config value field from bool to boolean to fix drivers
  build failures due to a conflict with C++ and stdbool.h

* Mon Dec 19 2022 Peter Hutterer <peter.hutterer@redhat.com> - 1.20.14-12
- Fix buggy patch to CVE-2022-46340

* Wed Dec 14 2022 Peter Hutterer <peter.hutterer@redhat.com> 1.20.14-11
- CVE fix for: CVE-2022-4283, CVE-2022-46340, CVE-2022-46341,
  CVE-2022-46342, CVE-2022-46343, CVE-2022-46344

* Wed Nov 23 2022 Peter Hutterer <peter.hutterer@redhat.com> - 1.20.14-10
- Drop dependency on xorg-x11-font-utils, it was only there for on
  build-time variable that's always the same value anyway (#2145088)

* Tue Nov  8 2022 Olivier Fourdan <ofourdan@redhat.com> - 1.20.14-9
- Fix CVE-2022-3550, CVE-2022-3551

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.20.14-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 12 2022 Olivier Fourdan <ofourdan@redhat.com> - 1.20.14-7
- Fix CVE-2022-2319/ZDI-CAN-16062, CVE-2022-2320/ZDI-CAN-16070

* Wed Apr 13 2022 Dominik Mierzejewski <rpm@greysector.net> - 1.20.14-6
- Don't hardcode fps for fake screen (#2054188)

* Fri Apr 8 2022 Jocelyn Falempe <jfalempe@redhat.com> - 1.20.14-5
- Fix basic graphic mode not working with simpledrm (#2067151)

* Fri Jan 28 2022 Olivier Fourdan <ofourdan@redhat.com> - 1.20.14-4
- Fix build with GCC 12 (#2047134)

* Tue Jan 25 2022 Olivier Fourdan <ofourdan@redhat.com> - 1.20.14-3
- Fix crash with NVIDIA proprietary driver with Present (#2046147)

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.20.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Dec 17 2021 Olivier <ofourdan@redhat.com> - 1.20.14-1
- xserver 1.20.14
  CVE-2021-4008/ZDI-CAN-14192 (#2026059, #2032941)
  CVE-2021-4009/ZDI-CAN-14950 (#2026072, #2032943)
  CVE-2021-4010/ZDI-CAN-14951 (#2026073, #2032944)
  CVE-2021-4011/ZDI-CAN-14952 (#2026074, #2032945)

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 1.20.11-3
- Rebuilt with OpenSSL 3.0.0

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.20.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Apr  14 2021 Olivier Fourdan <ofourdan@redhat.com> - 1.20.11-1
- xserver 1.20.11 (CVE-2021-3472 / ZDI-CAN-1259)

* Wed Feb 03 2021 Peter Hutterer <peter.hutterer@redhat.com> 1.20.10-5
- Drop BuildRequires for flex-devel (#1871101)

* Mon Feb  1 2021 Olivier Fourdan <ofourdan@redhat.com> - 1.20.10-4
- Remove Xwayland from the xserver builds

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.20.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jan 19 2021 Adam Jackson <ajax@redhat.com> - 1.20.10-2
- Disable int10 and vbe on RHEL
- Disable DRI1
- Stop overriding the vendor name

* Wed Dec  2 2020 Olivier Fourdan <ofourdan@redhat.com> - 1.20.10-1
- xserver 1.20.10 (CVE-2020-14360, CVE-2020-25712)

* Thu Nov  5 10:35:09 AEST 2020 Peter Hutterer <peter.hutterer@redhat.com> - 1.20.9-3
- Add BuildRequires for make

* Wed Nov 04 2020 Peter Hutterer <peter.hutterer@redhat.com> 1.20.9-2
- Drop BuildRequires to git-core only

* Thu Oct  8 2020 Olivier Fourdan <ofourdan@redhat.com> - 1.20.9-1
- xserver 1.20.9 + all current fixes from upstream

* Wed Aug 12 2020 Adam Jackson <ajax@redhat.com> - 1.20.8-4
- Enable XC-SECURITY

* Fri Jul 31 2020 Adam Jackson <ajax@redhat.com> - 1.20.8-3
- Fix information disclosure bug in pixmap allocation (CVE-2020-14347)

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.20.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Mar 30 2020 Olivier Fourdan <ofourdan@redhat.com> - 1.20.8-1
- xserver 1.20.8
- Backport latest Xwayland randr resolution change emulation support
  patches.

* Wed Mar 18 2020 Olivier Fourdan <ofourdan@redhat.com> - 1.20.7-2
- Fix a crash on closing a window using Present found upstream:
  https://gitlab.freedesktop.org/xorg/xserver/issues/1000

* Fri Mar 13 2020 Olivier Fourdan <ofourdan@redhat.com> - 1.20.7-1
- xserver 1.20.7
- backport from stable "xserver-1.20-branch" up to commit ad7364d8d
  (for mutter fullscreen unredirect on Wayland)
- Update videodrv minor ABI as 1.20.7 changed the minor ABI version
  (backward compatible, API addition in glamor)
- Rebase Xwayland randr resolution change emulation support patches

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.20.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov 25 2019 Olivier Fourdan <ofourdan@redhat.com> - 1.20.6-1
- xserver 1.20.6

* Mon Nov  4 2019 Hans de Goede <hdegoede@redhat.com> - 1.20.5-9
- Fix building with new libglvnd-1.2.0 (E)GL headers and pkgconfig files

* Mon Nov  4 2019 Hans de Goede <hdegoede@redhat.com> - 1.20.5-8
- Backport Xwayland randr resolution change emulation support

* Thu Aug 29 2019 Olivier Fourdan <ofourdan@redhat.com> 1.20.5-7
- Pick latest fixes from xserver stable branch upstream (rhbz#1729925)

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.20.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul  8 2019 Olivier Fourdan <ofourdan@redhat.com> 1.20.5-5
- Do not include <sys/io.h> on ARM with glibc to avoid compilation failure.
- Do not force vbe and int10 sdk headers as this enables int10 which does
  not build on ARM without <sys/io.h>

* Mon Jul  8 2019 Olivier Fourdan <ofourdan@redhat.com> 1.20.5-4
- Fix regression causing screen tearing with upstream xserver 1.20.5
  (rhbz#1726419)

* Fri Jun 28 2019 Olivier Fourdan <ofourdan@redhat.com> 1.20.5-3
- Remove atomic downstream patches causing regressions (#1714981, #1723715)
- Xwayland crashes (#1708119, #1691745)
- Cursor issue with tablet on Xwayland
- Xorg/modesetting issue with flipping pixmaps with Present (#1645553)

* Thu Jun 06 2019 Peter Hutterer <peter.hutterer@redhat.com> 1.20.5-2
- Return AlreadyGrabbed for keycodes > 255 (#1697804)

* Thu May 30 2019 Adam Jackson <ajax@redhat.com> - 1.20.5-1
- xserver 1.20.5

* Tue Apr 23 2019 Adam Jackson <ajax@redhat.com> - 1.20.4-4
- Fix some non-atomic modesetting calls to be atomic

* Wed Mar 27 2019 Peter Hutterer <peter.hutterer@redhat.com> 1.20.4-3
- Fix a Qt scrolling bug, don't reset the valuator on slave switch

* Thu Mar 21 2019 Adam Jackson <ajax@redhat.com> - 1.20.4-2
- Backport an Xwayland crash fix in the Present code

* Tue Feb 26 2019 Adam Jackson <ajax@redhat.com> - 1.20.4-1
- xserver 1.20.4

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.20.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 11 2019 Olivier Fourdan <ofourdan@redhat.com> - 1.20.3-3
- More Xwayland/Present fixes from upstream (rhbz#1609181, rhbz#1661748)

* Thu Dec 06 2018 Olivier Fourdan <ofourdan@redhat.com> - 1.20.3-2
- Xwayland/Present fixes from master upstream

* Thu Nov 01 2018 Adam Jackson <ajax@redhat.com> - 1.20.3-1
- xserver 1.20.3

* Mon Oct 15 2018 Adam Jackson <ajax@redhat.com> - 1.20.2-1
- xserver 1.20.2

* Thu Oct  4 2018 Hans de Goede <hdegoede@redhat.com> - 1.20.1-4
- Rebase patch to use va_gl as vdpau driver on i965 GPUs, re-fix rhbz#1413733

* Thu Sep 13 2018 Dave Airlie <airlied@redhat.com> - 1.20.1-3
- Build with PIE enabled (this doesn't enable bind now)

* Mon Sep 10 2018 Olivier Fourdan <ofourdan@redhat.com> - 1.20.1-2
- Include patches from upstream to fix Xwayland crashes

* Thu Aug 09 2018 Adam Jackson <ajax@redhat.com> - 1.20.1-1
- xserver 1.20.1

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.20.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 12 2018 Adam Jackson <ajax@redhat.com> - 1.20.0-4
- Xorg and Xwayland Requires: libEGL

* Fri Jun 01 2018 Adam Williamson <awilliam@redhat.com> - 1.20.0-3
- Backport fixes for RHBZ#1579067

* Wed May 16 2018 Adam Jackson <ajax@redhat.com> - 1.20.0-2
- Xorg Requires: xorg-x11-drv-libinput

* Thu May 10 2018 Adam Jackson <ajax@redhat.com> - 1.20.0-1
- xserver 1.20

* Wed Apr 25 2018 Adam Jackson <ajax@redhat.com> - 1.19.99.905-2
- Fix xvfb-run's default depth to be 24

* Tue Apr 24 2018 Adam Jackson <ajax@redhat.com> - 1.19.99.905-1
- xserver 1.20 RC5

* Thu Apr 12 2018 Olivier Fourdan <ofourdan@redhat.com> - 1.19.99.904-2
- Re-fix "use type instead of which in xvfb-run (rhbz#1443357)" which
  was overridden inadvertently

* Tue Apr 10 2018 Adam Jackson <ajax@redhat.com> - 1.19.99.904-1
- xserver 1.20 RC4

* Mon Apr 02 2018 Adam Jackson <ajax@redhat.com> - 1.19.99.903-1
- xserver 1.20 RC3

* Tue Feb 13 2018 Olivier Fourdan <ofourdan@redhat.com> 1.19.6-5
- xwayland: avoid race condition on new keymap
- xwayland: Keep separate variables for pointer and tablet foci (rhbz#1519961)
- xvfb-run now support command line option “--auto-display”

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.19.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 30 2018 Olivier Fourdan <ofourdan@redhat.com> 1.19.6-3
- Avoid generating a core file when the Wayland compositor is gone.

* Thu Jan 11 2018 Peter Hutterer <peter.hutterer@redhat.com> 1.19.6-2
- Fix handling of devices with ID_INPUT=null

* Wed Dec 20 2017 Adam Jackson <ajax@redhat.com> - 1.19.6-1
- xserver 1.19.6

* Thu Oct 12 2017 Adam Jackson <ajax@redhat.com> - 1.19.5-1
- xserver 1.19.5

* Thu Oct 05 2017 Olivier Fourdan <ofourdan@redhat.com> - 1.19.4-1
- xserver-1.19.4
- Backport tablet support for Xwayland

* Fri Sep 08 2017 Troy Dawson <tdawson@redhat.com> - 1.19.3-9
- Cleanup spec file conditionals

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.19.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.19.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jul  2 2017 Ville Skyttä <ville.skytta@iki.fi> - 1.19.3-6
- Use type instead of which in xvfb-run (rhbz#1443357)

* Thu May 04 2017 Orion Poplawski <orion@cora.nwra.com> - 1.19.3-5
- Enable full build for s390/x

* Mon Apr 24 2017 Ben Skeggs <bskeggs@redhat.com> - 1.19.3-4
- Default to xf86-video-modesetting on GeForce 8 and newer

* Fri Apr 07 2017 Adam Jackson <ajax@redhat.com> - 1.19.3-3
- Inoculate against a versioning bug with libdrm 2.4.78

* Thu Mar 23 2017 Hans de Goede <hdegoede@redhat.com> - 1.19.3-2
- Use va_gl as vdpau driver on i965 GPUs (rhbz#1413733)

* Wed Mar 15 2017 Adam Jackson <ajax@redhat.com> - 1.19.3-1
- xserver 1.19.3

* Thu Mar 02 2017 Adam Jackson <ajax@redhat.com> - 1.19.2-1
- xserver 1.19.2

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.19.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 01 2017 Peter Hutterer <peter.hutterer@redhat.com> 1.19.1-3
- Fix a few input thread lock issues causing intel crashes (#1384486)

* Mon Jan 16 2017 Adam Jackson <ajax@redhat.com> - 1.19.1-2
- Limit the intel driver only on F26 and up

* Wed Jan 11 2017 Adam Jackson <ajax@redhat.com> - 1.19.1-1
- xserver 1.19.1

* Tue Jan 10 2017 Hans de Goede <hdegoede@redhat.com> - 1.19.0-4
- Follow Debian and only default to the intel ddx on gen4 or older intel GPUs

* Tue Dec 20 2016 Hans de Goede <hdegoede@redhat.com> - 1.19.0-3
- Add one more patch for better integration with the nvidia binary driver

* Thu Dec 15 2016 Hans de Goede <hdegoede@redhat.com> - 1.19.0-2
- Add some patches for better integration with the nvidia binary driver
- Add a patch from upstream fixing a crash (rhbz#1389886)

* Wed Nov 23 2016 Olivier Fourdan <ofourdan@redhat.com> 1.19.0-1
- xserver 1.19.0
- Fix use after free of cursors in Xwayland (rhbz#1385258)
- Fix an issue where some monitors would show only black, or
  partially black when secondary GPU outputs are used

* Tue Nov 15 2016 Peter Hutterer <peter.hutterer@redhat.com> 1.19.0-0.8.rc2
- Update device barriers for new master devices (#1384432)

* Thu Nov  3 2016 Hans de Goede <hdegoede@redhat.com> - 1.19.0-0.7.rc2
- Update to 1.19.0-rc2
- Fix (hopefully) various crashes in FlushAllOutput() (rhbz#1382444)
- Fix Xwayland crashing in glamor on non glamor capable hw (rhbz#1390018)

* Tue Nov  1 2016 Ben Crocker <bcrocker@redhat.com> - 1.19.0-0.6.20161028
- Fix Config record allocation during startup: if xorg.conf.d directory
- was absent, a segfault resulted.

* Mon Oct 31 2016 Adam Jackson <ajax@redhat.com> - 1.19.0-0.5.20161026
- Use %%autopatch instead of doing our own custom git-am trick

* Fri Oct 28 2016 Hans de Goede <hdegoede@redhat.com> - 1.19.0-0.4.20161026
- Add missing Requires: libXfont2-devel to -devel sub-package (rhbz#1389711)

* Wed Oct 26 2016 Hans de Goede <hdegoede@redhat.com> - 1.19.0-0.3.20161026
- Sync with upstream git, bringing in a bunch if bug-fixes
- Add some extra fixes which are pending upstream
- This also adds PointerWarping emulation to Xwayland, which should improve
  compatiblity with many games
