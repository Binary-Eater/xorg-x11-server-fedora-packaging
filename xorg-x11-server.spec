# F8 TODO list:
#
# Fix rhpxl to no longer need vesamodes/extramodes
# RHEL5 bugfix sync
# --enable-kdrive just for Xephyr is overkill, should fix that upstream

%define pkgname xorg-server

Summary:   X.Org X11 X server
Name:      xorg-x11-server
Version:   1.3.0.0
Release:   43%{?dist}
URL:       http://www.x.org
License:   MIT
Group:     User Interface/X
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:   ftp://ftp.x.org/pub/individual/xserver/%{pkgname}-%{version}.tar.bz2
Source100: comment-header-modefiles.txt

# general bug fixes
Patch0:    xorg-x11-server-0.99.3-init-origins-fix.patch
Patch5:    xorg-x11-server-libxf86config-dont-write-empty-sections.patch
Patch6:    xorg-x11-server-1.1.1-builderstring.patch
Patch7:    xorg-x11-server-1.1.1-xkb-in-xnest.patch
Patch10:   xorg-x11-server-1.1.1-vbe-filter-less.patch
Patch11:   xorg-x11-server-1.1.1-vt-activate-is-a-terrible-api.patch
Patch12:   xorg-x11-server-1.1.1-graphics-expose.patch
Patch15:   xorg-x11-server-1.1.1-automake-1.10-fixes.patch
Patch19:   xserver-1.3.0-xnest-exposures.patch
Patch20:   xserver-1.3.0-x86emu-imul-int64.patch
Patch21:   xserver-1.3.0-xkb-and-loathing.patch
Patch22:   xserver-1.3.0-fbdevhw-magic-numbers.patch
Patch23:   xserver-1.3.0-ramdac-export.patch
Patch24:   xserver-1.3.0-reput-video.patch
Patch25:   xserver-1.3.0-xrandr-timestamp-buglet.patch

# OpenGL compositing manager feature/optimization patches.
Patch100:  xorg-x11-server-1.1.0-no-move-damage.patch
Patch101:  xorg-x11-server-1.1.0-dont-backfill-bg-none.patch
Patch105:  xorg-x11-server-1.2.0-enable-composite.patch
Patch106:  xorg-x11-server-1.1.1-no-composite-in-xnest.patch
Patch108:  xserver-1.3.0-no-pseudocolor-composite.patch

# Red Hat specific tweaking, not intended for upstream
# XXX move these to the end of the list
Patch1001:  xorg-x11-server-Red-Hat-extramodes.patch
Patch1002:  xorg-x11-server-1.2.0-xephyr-only.patch
Patch1003:  xorg-x11-server-1.0.1-fpic-libxf86config.patch
Patch1004:  xorg-x11-server-1.2.0-selinux-awareness.patch
Patch1005:  xorg-x11-server-1.1.1-builtin-fonts.patch
Patch1006:  xorg-x11-server-1.1.1-no-scanpci.patch
Patch1007:  xorg-x11-server-1.1.1-spurious-libxf1bpp-link.patch
Patch1008:  xorg-x11-server-1.2.0-xf86config-comment-less.patch
Patch1010:  xserver-1.3.0-no-prerelease-warning.patch
Patch1011:  xserver-1.3.0-composite-version.patch
Patch1012:  xserver-1.3.0-mesa7.patch
Patch1013:  xserver-1.3.0-exaupgrade.patch
Patch1014:  xserver-1.3.0-newglx-offscreen-pixmaps.patch
Patch1015:  xserver-1.3.0-randr-updates.patch
Patch1022:  xserver-1.3.0-default-dpi.patch
Patch1023:  xserver-1.3.0-randr-preferred-mode-fix.patch
Patch1024:  xserver-1.3.0-avoid-ps2-probe.patch
Patch1025:  xserver-1.3.0-ignore-extra-entity.patch
Patch1026:  xserver-1.3.0-randr-fix-set-rotations-xinerama.patch

Patch2001:  xserver-1.2.0-geode-mmx.patch
Patch2002:  xserver-1.2.0-xephyr-keysym-madness.patch
Patch2003:  xserver-1.2.0-vfprintf.patch
Patch2004:  xserver-1.3.0-honor-displaysize.patch
Patch2007:  xserver-1.3.0-randr12-config-hack.patch
Patch2008:  xserver-1.3.0-randrama-no-zero-screens.patch
Patch2009:  xserver-1.3.0-arm-iopl.patch
Patch2010:  xserver-1.3.0-idletime.patch
Patch2012:  xserver-1.3.0-add-really-slow-bcopy.patch
Patch2013:  xserver-1.3.0-document-fontpath-correctly.patch
Patch2014:  xserver-1.3.0-intel-by-default.patch
Patch2015:  xserver-1.3.0-accidental-abi.patch
Patch2016:  xserver-1.3.0-xorg-conf-man-randr-update.patch
Patch2017:  xserver-1.3.0-update-quirks.patch
Patch2018:  xserver-1.3.0-late-sigusr1.patch
Patch2019:  xserver-1.3.0-yet-more-vt-ioctl-hate.patch
Patch2020:  xserver-1.3.0-update-edid-quirks.patch
Patch2021:  xorg-server-1.3.0.0-prefer-openchrome-ugly-hack.patch
Patch2022:  xorg-server-1.3.0.0-0001-X86EMU-handle-CPUID-instruction.patch
Patch2023:  xorg-server-1.3.0.0-0003-X86EMU-when-emulating-PCI-access-use-the-correct-d.patch
Patch2024:  xorg-server-1.3.0.0-0002-X86EMU-added-blacklist-for-I-O-port-in-0-0xFF-range.patch
Patch2025:  xorg-server-1.3.0.0-geode-gx2-lx-autodetect.patch

# assorted PCI layer shenanigans.  oh the pain.
Patch2500:  xorg-x11-server-1.2.99-unbreak-domain.patch
Patch2501:  xserver-1.3.0-pci-bus-count.patch
Patch2502:  xserver-1.3.0-mmap-failure-check.patch
Patch2503:  xserver-1.3.0-rom-search.patch
Patch2504:  xserver-1.3.0-domain-obiwan.patch
Patch2505:  xserver-1.3.0-pci-device-enable.patch

# CVEs
Patch3000:  cve-2007-5760.patch
Patch3001:  cve-2007-5958.patch
Patch3002:  cve-2007-6427.patch
Patch3003:  cve-2007-6428.patch
Patch3004:  cve-2007-6429.patch
Patch3005:  cve-2008-0006-server-fixup.patch
Patch3006:  cve-2007-3920.patch

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

%define xservers --enable-xvfb --enable-xnest --enable-kdrive --enable-xephyr --enable-dmx

# FIXME: Temporary Build deps on autotools, as needed...
BuildRequires: automake autoconf libtool

BuildRequires: pkgconfig
BuildRequires: xorg-x11-util-macros >= 1.1.5

BuildRequires: xorg-x11-proto-devel >= 7.1-11
BuildRequires: randrproto >= 1.2
BuildRequires: fixesproto >= 4.0
BuildRequires: damageproto >= 1.1
BuildRequires: scrnsaverproto >= 1.1
BuildRequires: kbproto >= 1.0.3

BuildRequires: xorg-x11-xtrans-devel >= 1.0.3-3
BuildRequires: libXfont-devel
BuildRequires: libXau-devel
BuildRequires: libxkbfile-devel
# libXres-devel needed for something that links to libXres that I never
# bothered to figure out yet
BuildRequires: libXres-devel
# libfontenc-devel needed for Xorg, but not specified by
# upstream deps.  Build fails without it.
BuildRequires: libfontenc-devel
# Required for Xtst examples
BuildRequires: libXtst-devel
# libXdmcp-devel needed for Xdmx, Xnest, Xephyr
BuildRequires: libXdmcp-devel
# libX11-devel needed for Xdmx, Xnest, Xephyr
BuildRequires: libX11-devel
# libXext-devel needed for Xdmx, Xnest, Xephyr
BuildRequires: libXext-devel
# XXX Really?  Why would we need this, Xfont should hide it.
BuildRequires: freetype-devel >= 2.1.9-1

# DMX config utils buildreqs.
BuildRequires: libXt-devel
BuildRequires: libdmx-devel
BuildRequires: libXmu-devel
BuildRequires: libXrender-devel
BuildRequires: libXi-devel
BuildRequires: libXpm-devel
BuildRequires: libXaw-devel
BuildRequires: libXfixes-devel

BuildRequires: mesa-libGL-devel >= 7.0.1
BuildRequires: mesa-source >= 7.0.1-6
# XXX silly...
BuildRequires: libdrm-devel >= 2.3.0
%if %{with_hw_servers}
Requires: libdrm >= 2.3.0
%endif

BuildRequires: libselinux-devel

# Make sure libXfont has the catalogue FPE
Requires: libXfont >= 1.2.9

# Make sure we pull ABI compatible drivers.
Conflicts: xorg-x11-drv-ati < 6.6.1
Conflicts: xorg-x11-drv-i810 < 1.6.0
# Match up work-arounds between compiz and the xserver
Conflicts: compiz < 0.0.13-0.20.20060817git.fc6
# Match up GLX_EXT_texture_from_pixmap opcodes
Conflicts: mesa-libGL < 6.5.1-2.fc6

# All server subpackages have a virtual provide for the name of the server
# they deliver.  The Xorg one is versioned, the others are intentionally
# unversioned.

%description
X.Org X11 X server

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
Obsoletes: XFree86 xorg-x11
# These drivers were dropped in F7 for being broken, so uninstall them.
Obsoletes: xorg-x11-drv-elo2300 <= 1.1.0-2.fc7
Obsoletes: xorg-x11-drv-joystick <= 1.1.0-2.fc7

%description Xorg
X.org X11 is an open source implementation of the X Window System.  It
provides the basic low level functionality which full fledged
graphical user interfaces (GUIs) such as GNOME and KDE are designed
upon.
%endif


%package Xnest
Summary: A nested server.
Group: User Interface/X
Obsoletes: XFree86-Xnest, xorg-x11-Xnest
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
Obsoletes: XFree86-Xvfb xorg-x11-Xvfb
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
%package sdk
Summary: SDK for X server driver module development
Group: User Interface/X
Obsoletes: XFree86-sdk xorg-x11-sdk
Requires: xorg-x11-util-macros
Requires: xorg-x11-proto-devel
Requires: pkgconfig
Requires(pre): xorg-x11-filesystem >= 0.99.2-3
Provides: libxf86config-devel = %{version}-%{release}

%description sdk
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
%setup -q -n %{pkgname}-%{version}
%patch0 -p0 -b .init-origins-fix
%patch5 -p0 -b .libxf86config-dont-write-empty-sections
%patch6 -p1 -b .builderstring
%patch7 -p1 -b .xkb-in-xnest
%patch10 -p1 -b .vbe-filter
%patch11 -p1 -b .vt-activate
%patch12 -p1 -b .graphics-expose
%patch15 -p1 -b .automake-1.10
%patch19 -p1 -b .xnest-expose
%patch20 -p1 -b .x86emu-imul
%patch21 -p1 -b .xkb-signal-loathing
%patch22 -p1 -b .magic-numbers
%patch23 -p1 -b .ramdac
%patch24 -p1 -b .reput
%patch25 -p1 -b .xrandr-timestamp

%patch100 -p0 -b .no-move-damage
%patch101 -p0 -b .dont-backfill-bg-none
%patch105 -p1 -b .enable-composite
%patch106 -p1 -b .no-xnest-composite
%patch108 -p1 -b .composite-paranoia

%patch1001 -p1 -b .Red-Hat-extramodes
%patch1002 -p1 -b .xephyr
%patch1003 -p1 -b .fpic
%patch1004 -p1 -b .selinux-awareness
%patch1005 -p0 -b .builtin-fonts
%patch1006 -p1 -b .no-scanpci
%patch1007 -p1 -b .xf1bpp
%patch1008 -p1 -b .comment-less
%patch1010 -p1 -b .prerelease-warning
%patch1011 -p1 -b .composite-version
%patch1012 -p1 -b .newmesa
%patch1013 -p1 -b .newexa
%patch1014 -p1 -b .offscreen-pixmaps
%patch1015 -p1 -b .randr-update
%patch1022 -p1 -b .dpi
%patch1023 -p1 -b .randr-preferred
%patch1024 -p1 -b .ps2-probe
%patch1025 -p1 -b .ignore-entities
%patch1026 -p1 -b .fix-set-rotation-crash

%patch2001 -p1 -b .geode-mmx
%patch2002 -p1 -b .xephyr-keysym
%patch2003 -p1 -b .vfprintf
%patch2004 -p1 -b .displaysize
%patch2007 -p1 -b .randrconfig
%patch2008 -p1 -b .randrama-zero-screens
%patch2009 -p1 -b .arm
%patch2010 -p1 -b .idletime
%patch2012 -p1 -b .slow-bcopy
%patch2013 -p1 -b .fontpath-doc
%patch2014 -p1 -b .intel
%patch2015 -p1 -b .accidental-abi
%patch2016 -p1 -b .document-randr
%patch2017 -p1 -b .update-quirk
%patch2018 -p1 -b .sigusr1
%patch2019 -p1 -b .vt-ioctl-hate
%patch2020 -p1 -b .more-quirk-patch
%patch2021 -p1 -b .prefer-openchrome-ugly-hack
%patch2022 -p1 -b .X86EMU-handle-CPUID-instruction
%patch2023 -p1 -b .X86EMU-added-blacklist
%patch2024 -p1 -b .X86EMU-when-emulating-PCI
%patch2025 -p1 -b .geode-gx2-lx-autodetect

%patch2500 -p1 -b .unbreak-domains
%patch2501 -p1 -b .pci-bus-count
%patch2502 -p1 -b .mmap-check
%patch2503 -p1 -b .rom-search
%patch2504 -p1 -b .domain-obiwan
%patch2505 -p1 -b .device-enable

%patch3000 -p1 -b .cve-2007-5760
%patch3001 -p1 -b .cve-2007-5958
%patch3002 -p1 -b .cve-2007-6427
%patch3003 -p1 -b .cve-2007-6428
%patch3004 -p1 -b .cve-2007-6429
%patch3005 -p1 -b .cve-2008-0006
%patch3006 -p1 -b .cve-2007-3920

%build

%if %{fedora} == 7
%define default_font_path "unix/:7100,catalogue:/etc/X11/fontpath.d,built-ins"
%else
%define default_font_path "catalogue:/etc/X11/fontpath.d,built-ins"
%endif

# --with-rgb-path should be superfluous now ?
# --with-pie ?
aclocal ; automake -a ; autoconf
%configure --enable-maintainer-mode \
	%{enable_xorg} \
	--disable-xprint --enable-xvfb --enable-xnest --enable-dmx \
	--enable-kdrive --enable-xephyr \
	--disable-static \
	--with-pic \
	--enable-composite \
	--enable-xtrap \
	--enable-xcsecurity \
	--enable-xevie \
	--with-int10=x86emu \
	--with-default-font-path=%{default_font_path} \
	--with-module-dir=%{moduledir} \
	--with-os-name="Fedora 8" \
	--with-os-vendor="Red Hat, Inc." \
	--with-builderstring="Build ID: %{name} %{version}-%{release}" \
	--with-xkb-output=%{_localstatedir}/lib/xkb \
	--with-rgb-path=%{_datadir}/X11/rgb \
	--disable-xorgcfg \
	--enable-install-libxf86config \
	--with-mesa-source=%{_datadir}/mesa/source \
%if %{with_hw_servers}
	--enable-dri \
	--with-dri-driver-path=%{drimoduledir} \
%endif
	${CONFIGURE}

make -s %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT moduledir=%{moduledir}


%if %{with_hw_servers}
mkdir -p $RPM_BUILD_ROOT%{_libdir}/xorg/modules/{drivers,input}

# Install the vesamodes and extramodes files to let our install/config tools
# be able to parse the same modelist as the X server uses (rhpxl).
mkdir -p $RPM_BUILD_ROOT%{_datadir}/xorg
for each in vesamodes extramodes ; do
    install -m 0644 %{SOURCE100} $RPM_BUILD_ROOT%{_datadir}/xorg/$each
    cat hw/xfree86/common/$each >> $RPM_BUILD_ROOT%{_datadir}/xorg/$each
    chmod 0444 $RPM_BUILD_ROOT%{_datadir}/xorg/$each
done
%endif

# Make the source package
%define xserver_source_dir %{_datadir}/xorg-x11-server-source
%define inst_srcdir %{buildroot}/%{xserver_source_dir}
mkdir -p %{inst_srcdir}/{Xext,xkb,GL,hw/xfree86/{common,utils/xorgconfig}}
cp cpprules.in %{inst_srcdir}
cp Xext/SecurityPolicy %{inst_srcdir}/Xext
cp xkb/README.compiled %{inst_srcdir}/xkb
cp GL/symlink-mesa.sh %{inst_srcdir}/GL
cp hw/xfree86/{xorgconf.cpp,Options} %{inst_srcdir}/hw/xfree86
cp hw/xfree86/common/{vesamodes,extramodes} %{inst_srcdir}/hw/xfree86/common
cp hw/xfree86/utils/xorgconfig/Cards{,98} %{inst_srcdir}/hw/xfree86/utils/xorgconfig/

find . -type f | egrep '.*\.(c|h|am|ac|inc|m4|h.in|pc.in|man.pre|pl)$' |
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

%ifarch s390 s390x
    # FIXME: The following files get installed on s390/s390x and we don't
    # want some of them on s390 at all, and others should be in a -common
    # subpackage, but it's not worth doing that for 3 files right now.
    # error: Installed (but unpackaged) file(s) found:
    #	   /randrstr.h
    #	   /usr/lib/pkgconfig/xorg-server.pc
    #	      /usr/share/aclocal/xorg-server.m4
    #	      /usr/share/man/man1/Xserver.1x.gz
    #	      /var/lib/xkb/README.compiled

    rm -f $RPM_BUILD_ROOT/randrstr.h
    rm -rf $RPM_BUILD_ROOT%{_libdir}/pkgconfig
    rm -rf $RPM_BUILD_ROOT%{_datadir}/aclocal
    rm -rf $RPM_BUILD_ROOT/var/lib/xkb
%endif
}

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with_hw_servers}
%pre Xorg
{
    pushd /etc/X11

    for configfile in XF86Config XF86Config-4 ; do
	if [ -r $configfile ]; then
	    if [ -r xorg.conf ]; then
		mv -f $configfile $configfile.obsoleted
	    else
		mv -f $configfile xorg.conf
	    fi
	fi
    done

    [ -e xorg.conf ] || return 0

    perl -p -i -e 's/^.*Load.*"(pex5|xie|xtt).*\n$"//gi' xorg.conf
    perl -p -i -e 's/^\s*Driver(.*)"keyboard"/Driver\1"kbd"/gi' xorg.conf
    perl -p -i -e 's/^.*Option.*"XkbRules".*"(xfree86|xorg)".*\n$//gi' xorg.conf
    perl -p -i -e 's#^\s*RgbPath.*$##gi' xorg.conf
    # lame, the nvidia driver needs to override this
    if ! grep -q 'ModulePath.*nvidia' xorg.conf ; then
      perl -p -i -e 's#^\s*ModulePath.*$##gi' xorg.conf
    fi

    popd
} &> /dev/null || :
%endif

# The Xserver.1 manpage is intentionally present in multiple subpackages.
# It could reasonably form part of a -common subpackage though.

%if %{with_hw_servers}
%files Xorg
%defattr(-,root,root,-)
%{_bindir}/X
%attr(4711, root, root) %{_bindir}/Xorg
%{_bindir}/gtf
%{_bindir}/cvt
%dir %{_datadir}/xorg
%{_datadir}/xorg/vesamodes
%{_datadir}/xorg/extramodes
%dir %{_libdir}/xorg
%dir %{_libdir}/xorg/modules
%dir %{_libdir}/xorg/modules/drivers
%dir %{_libdir}/xorg/modules/extensions
%{_libdir}/xorg/modules/extensions/libGLcore.so
%{_libdir}/xorg/modules/extensions/libglx.so
%{_libdir}/xorg/modules/extensions/libdri.so
%{_libdir}/xorg/modules/extensions/libdbe.so
%{_libdir}/xorg/modules/extensions/libextmod.so
%{_libdir}/xorg/modules/extensions/librecord.so
%{_libdir}/xorg/modules/extensions/libxtrap.so
%dir %{_libdir}/xorg/modules/input
%dir %{_libdir}/xorg/modules/fonts
%{_libdir}/xorg/modules/fonts/libfreetype.so
%{_libdir}/xorg/modules/fonts/libtype1.so
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
%{_libdir}/xorg/modules/libafb.so
%{_libdir}/xorg/modules/libcfb.so
%{_libdir}/xorg/modules/libcfb32.so
%{_libdir}/xorg/modules/libexa.so
%{_libdir}/xorg/modules/libfb.so
%{_libdir}/xorg/modules/libint10.so
%{_libdir}/xorg/modules/libmfb.so
%{_libdir}/xorg/modules/libpcidata.so
%{_libdir}/xorg/modules/libshadow.so
%{_libdir}/xorg/modules/libshadowfb.so
%{_libdir}/xorg/modules/libvbe.so
%{_libdir}/xorg/modules/libvgahw.so
%{_libdir}/xorg/modules/libxaa.so
%{_libdir}/xorg/modules/libxf1bpp.so
%{_libdir}/xorg/modules/libxf4bpp.so
%{_libdir}/xorg/modules/libxf8_16bpp.so
%{_libdir}/xorg/modules/libxf8_32bpp.so
%dir %{_libdir}/xserver
%{_libdir}/xserver/SecurityPolicy
%{_mandir}/man1/gtf.1*
%{_mandir}/man1/Xorg.1*
%{_mandir}/man1/Xserver.1*
%{_mandir}/man1/cvt.1*
%{_mandir}/man4/fbdevhw.4*
%{_mandir}/man4/exa.4*
%{_mandir}/man5/xorg.conf.5*
%dir %{_localstatedir}/lib/xkb
%{_localstatedir}/lib/xkb/README.compiled
%endif


%files Xnest
%defattr(-,root,root,-)
%{_bindir}/Xnest
%{_mandir}/man1/Xnest.1*
%{_mandir}/man1/Xserver.1*


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
%{_mandir}/man1/Xserver.1*


%files Xvfb
%defattr(-,root,root,-)
%{_bindir}/Xvfb
%{_mandir}/man1/Xvfb.1*
%{_mandir}/man1/Xserver.1*
%if !%{with_hw_servers}
%dir %{_libdir}/xserver
%{_libdir}/xserver/SecurityPolicy
%endif


%files Xephyr
%defattr(-,root,root,-)
%{_bindir}/Xephyr
%{_mandir}/man1/Xserver.1*


%if %{with_hw_servers}
%files sdk
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
* Sun Mar 02 2008 Warren Togami <wtogami@redhat.com> 1.3.0.0-43
- xorg-server-1.3.0.0-prefer-openchrome-ugly-hack.patch:
  Prefer openchrome to via driver during autoconfiguration.
- xorg-server-1.3.0.0-0001-X86EMU-handle-CPUID-instruction.patch
  xorg-server-1.3.0.0-0002-X86EMU-added-blacklist-for-I-O-port-in-0-0xFF-range.patch
  xorg-server-1.3.0.0-0003-X86EMU-when-emulating-PCI-access-use-the-correct-d.patch
  X86EMU fixes that allow amd driver work with a few broken BIOS
- xorg-server-1.3.0.0-geode-gx2-lx-autodetect.patch:
  Autoconfigure AMD Geode GX2 100b:0030
                AMD Geode LX  1022:2081

* Tue Feb 12 2008 Adam Jackson <ajax@redhat.com> 1.3.0.0-42
- xserver-1.3.0-avoid-ps2-probe.patch: Delete an irrelevant hunk against
  the module loader that broke Xorg -configure.  (#397461)

* Mon Feb 11 2008 Adam Jackson <ajax@redhat.com> 1.3.0.0-41
- xserver-1.3.0-xorg-conf-man-randr-update.patch: Various fixes. (#429988)

* Mon Jan 21 2008 Kristian Høgsberg <krh@redhat.com> - 1.3.0.0-40
- cve-2007-3920.patch: Don't break grabs when redirecting windows.

* Fri Jan 18 2008 Dave Airlie <airlied@redhat.com> 1.3.0.0-39
- cve-2007-6429.patch: Fix patch to not break java apps

* Fri Jan 18 2008 Dave Airlie <airlied@redhat.com> 1.3.0.0-38
- cve-2007-5760.patch: XFree86-Misc Extension Invalid Array Index Vulnerability
- cve-2007-5958.patch: Xorg / XFree86 file existence disclosure vulnerability
- cve-2007-6427.patch: XInput Extension Memory Corruption Vulnerability
- cve-2007-6428.patch: TOG-CUP Extension Memory Corruption Vulnerability
- cve-2007-6429.patch: EVI and MIT-SHM Extension Integer Overflow Vulnerability
- cve-2008-0006-server-fixup.patch: PCF Font Vulnerability - this patch isn't strictly required with new version of libXfont.

* Thu Dec 13 2007 Adam Jackson <ajax@redhat.com> 1.3.0.0-37
- xorg-x11-server-Red-Hat-extramodes.patch: Remove the non-CVT-R timings
  for 1920x1080 and 1920x1200, they don't fit in a single DVI link and
  are therefore useless.

* Fri Nov 30 2007 Dave Airlie <airlied@redhat.com> 1.3.0.0-36
- xserver-1.3.0-update-edid-quirks.patch - updates quirk from master server

* Thu Nov 29 2007 Dave Airlie <airlied@redhat.com> 1.3.0.0-35
- xserver-1.3.0-ignore-extra-entity.patch - if a driver doesn't support 
  secondary entities, don't fatal error just ignore and keep going
- xserver-1.3.0-randr-fix-set-rotations-xinerama.patch - attempt to stop xinerama segfaulting randr12

* Thu Nov 01 2007 Adam Jackson <ajax@redhat.com> 1.3.0.0-34
- xserver-1.3.0-yet-more-vt-ioctl-hate.patch: You don't even want to know.

* Thu Oct 18 2007 Dave Airlie <airlied@redhat.com> 1.3.0.0-33
- xserver-1.3.0-xorg-conf-man-randr-update.patch - update man page for randr setup
- xserver-1.3.0-update-quirks.patch - update quirks for more monitor issues
- BuildReq: mesa-source >= 7.0.1-6.

* Mon Oct 15 2007 Adam Jackson <ajax@redhat.com> 1.3.0.0-31.jx
- xserver-1.3.0-late-sigusr1.patch: Test, move kill(getppid(), SIGUSR1)
  as late as possible.

* Fri Oct 12 2007 Adam Jackson <ajax@redhat.com> 1.3.0.0-31
- xorg-x11-server-Red-Hat-extramodes.patch: Remove 2560x1600 GTF timing.

* Thu Oct 11 2007 Adam Jackson <ajax@redhat.com> 1.3.0.0-30
- xserver-1.3.0-avoid-ps2-probe.patch: /dev/input/mice is always ExplorerPS/2,
  so don't waste time on startup probing for it.

* Fri Oct 05 2007 Adam Jackson <ajax@redhat.com> 1.3.0.0-29
- xserver-1.3.0-randr-preferred-mode-fix.patch: Fix infinite loop on X
  startup when a mode is requested in the config file. (#318731)
- Fix License tag.

* Wed Oct 03 2007 Adam Jackson <ajax@redhat.com> 1.3.0.0-28
- xserver-1.3.0-accidental-abi.patch: Make sure some symbols from parser/
  get exported, since apparently the intel driver uses them despite their
  not being in the documented ABI list.  Thanks guys.

* Mon Oct 01 2007 Adam Jackson <ajax@redhat.com> 1.3.0.0-27
- BuildReq: mesa-source >= 7.0.1-5.

* Wed Sep 26 2007 Adam Jackson <ajax@redhat.com> 1.3.0.0-26
- xserver-1.3.0-randr-updates.patch: Default ModeDebug to TRUE, better to
  have too much information than too little.
- xorg-x11-server-1.0.1-fpic-libxf86config.patch: Build the parser library
  with hidden symbols to shrink pyf86config a bit.
- xserver-1.3.0-intel-by-default.patch: Use intel, not i810, when starting
  without a config file.
- Enable maintainer mode when building so I swear at autotools less.

* Wed Sep 26 2007 Dave Airlie <airlied@redhat.com> 1.3.0.0-25
- xserver-1.3.0-randr-updates.patch: Backport randr from server git
  This contains a lot of fixes since 1.3.0 went out, and saves
  us backporting each fix individually
- xserver-1.3.0-less-randr-fakerama.patch - dropped
- xorg-x11-server-1.2.0-maxpixclock-option.patch - dropped
- xserver-1.3.0-edid-quirk-backports.patch - dropped
- xserver-1.2.0-honor-displaysize.patch - dropped
- xserver-1.3.0-honor-displaysize.patch - reapply to new code layout
- xserver-1.3.0-randr12-config-hack.patch - rebased

* Mon Sep 17 2007 Adam Jackson <ajax@redhat.com> 1.3.0.0-24
- xserver-1.3.0-edid-quirk-backports.patch: Update the EDID quirks code
  to match current git.

* Thu Sep 06 2007 Adam Jackson <ajax@redhat.com> 1.3.0.0-23
- xserver-1.3.0-xrandr-timestamp-buglet.patch: Make sure xrandr doesn't
  stop working after several hours. (Marius Gedminas, #273801)

* Fri Aug 24 2007 Adam Jackson <ajax@redhat.com> 1.3.0.0-22
- Bump BuildRequires: xorg-x11-xtrans-devel to pull in abstract socket
  support.

* Thu Aug 23 2007 Adam Jackson <ajax@redhat.com> 1.3.0.0-21
- xserver-1.3.0-document-fontpath-correctly.patch: Fix man page to point to
  directories that exist. (#251203, Matěj Cepl)

* Wed Aug 15 2007 Dave Airlie <airlied@redhat.com> 1.3.0.0-20
- xserver-1.3.0-newglx-offscreen-pixmaps.patch: fix zero-copy TFP again

* Tue Aug 14 2007 Adam Jackson <ajax@redhat.com> 1.3.0.0-19
- xserver-1.3.0-newglx-offscreen-pixmaps.patch: Zero-copy TFP is busted
  on at least my laptop, so turn it off again.

* Mon Aug 13 2007 Dave Airlie <airlied@redhat.com> 1.3.0.0-18
- xserver-1.3.0-mesa7.patch: Add support for building against mesa 7.0.1
  along with DRI zero-copy TFP hopefully
- xserver-1.3.0-exaupgrade.patch: Add updated EXA support
- dropped xserver-1.2.99.901-xephyr-crash-at-exit.patch - upstream
- rebase xorg-x11-server-1.1.1-offscreen-pixmaps.patch to xserver-1.3.0-newglx-offscreen-pixmaps.patch
- dropped xorg-x11-server-1.1.1-glcore-visual-matching.patch - fixed upstream

* Thu Aug 09 2007 Adam Jackson <ajax@redhat.com> 1.3.0.0-17
- xserver-1.3.0-default-dpi.patch: Switch default DPI to 100, on the
  principle that 75 is almost never right and 100 is much more likely.

* Thu Aug 02 2007 Dave Airlie <airlied@redhat.com> 1.3.0.0-16
- xserver-1.3.0-add-really-slow-bcopy.patch: Speed server start on some cards

* Thu Jul 12 2007 Adam Jackson <ajax@redhat.com> 1.3.0.0-15
- xserver-1.3.0-edid-quirk-backports.patch: Backport EDID quirks from
  master; fixes some Samsung monitors. (#232810)

* Thu Jul 12 2007 Adam Jackson <ajax@redhat.com> 1.3.0.0-14
- xserver-1.3.0-composite-version.patch: Force the server to report the
  Composite extension version it supports, not simply the version defined
  by the protocol headers it was built against.

* Mon Jul 02 2007 Adam Jackson <ajax@redhat.com> 1.3.0.0-13
- Add IDLETIME sync counter for great powersaving justice.
- Conditionalise default font path for F7 spec compatibility.

* Wed Jun 27 2007 Adam Jackson <ajax@redhat.com> 1.3.0.0-12
- Tweak %%post Xorg slightly to not demolish ModulePath lines installed by
  the nvidia driver.  (#244359)

* Wed Jun 27 2007 Adam Jackson <ajax@redhat.com> 1.3.0.0-11
- Obsolete the joystick and elo2300 drivers, they never worked and shouldn't
  be installed.

* Fri Jun 22 2007 Kristian Høgsberg <krh@redhat.com> - 1.3.0.0-10
- Change the default font path to catalogue:/etc/X11/fontpath.d,built-ins
- Drop build dependency xorg-x11-font-utils.

* Mon Jun 11 2007 Adam Jackson <ajax@redhat.com> 1.3.0.0-9
- xserver-1.3.0-reput-video.patch: Don't crash when minimizing an Xv
  window. (#241214)

* Wed Jun 06 2007 Adam Jackson <ajax@redhat.com> 1.3.0.0-8
- xserver-1.3.0-ramdac-export.patch: Make sure the old ramdac symbols are
  exported, since they're in-server now. (#242800)

* Mon Jun 04 2007 Adam Jackson <ajax@redhat.com> 1.3.0.0-7
- xserver-1.3.0-randrama-no-zero-screens.patch: For RANDR 1.2's fake
  Xinerama info, don't report Xinerama as being active if there are no
  RANDR 1.2 CRTCs active for that screen.  (#234567)
- xserver-1.3.0-arm-iopl.patch: Add __arm__ conditionals to many #ifdefs.

* Sat May 26 2007 Adam Jackson <ajax@redhat.com> 1.3.0.0-6
- Make sdk subpackage Require: pkgconfig.  Spotted in review for
  xorg-x11-drv-apm. (#226577)

* Fri May 11 2007 Adam Jackson <ajax@redhat.com> 1.3.0.0-5
- xserver-1.3.0-fbdevhw-magic-numbers.patch: If the fbdev driver claims to
  have a zero pixel clock, believe it.  Fixes Xen paravirt. (#238451)

* Mon May 07 2007 Adam Jackson <ajax@redhat.com> 1.3.0.0-4
- xorg-x11-server-1.1.1-offscreen-pixmaps.patch: Fix a crash when activating
  GLX_EXT_texture_from_pixmap without XAA.
- xserver-1.3.0-randr12-config-hack.patch: If a Modes line is given in
  the Screen section, and no PreferredMode option is given for a RANDR 1.2
  monitor, use the first mode in the Modes line as the preferred mode.
  Fixes anaconda ugliness on monitors larger than 800x600. (#238991)

* Mon Apr 30 2007 Adam Jackson <ajax@redhat.com> 1.3.0.0-3
- xserver-1.3.0-xkb-and-loathing.patch: Ignore (not just block) SIGALRM
  around calls to Popen()/Pclose().  Fixes a hang in openoffice when
  opening menus.
- Modify BuildRequires to use the virtual protocol Provides.

* Wed Apr 25 2007 Adam Jackson <ajax@redhat.com> 1.3.0.0-2
- xserver-1.3.0-less-randr-fakerama.patch: Disable RANDR's fake Xinerama
  geometry when there's more than one protocol screen. (#231257)

* Mon Apr 23 2007 Adam Jackson <ajax@redhat.com> 1.3.0.0-1
- xserver 1.3.0.

* Fri Apr 13 2007 Adam Jackson <ajax@redhat.com> 1.2.99.905-5
- xserver-rc5-to-now.patch: Updates from git.

* Wed Apr 11 2007 Adam Jackson <ajax@redhat.com> 1.2.99.905-4
- xserver-1.3.0-no-prerelease-warning.patch: Hush the useless prerelease
  warning if we happen to be building one (and even if not).
- xserver-1.3.0-pci-device-enable.patch: Make sure the PCI device is enabled
  in sysfs before we start touching it, otherwise, armageddon.

* Tue Apr 10 2007 Adam Jackson <ajax@redhat.com> 1.2.99.905-3
- xserver-1.3.0-domain-obiwan.patch: Fix a PCI domain off-by-one. (#235861)
- xserver-1.3.0-x86emu-imul-int64.patch: Fix imul in x86emu. (#235861)

* Mon Apr 09 2007 Adam Jackson <ajax@redhat.com> 1.2.99.905-2
- xserver-1.3.0-pci-bus-count.patch: Allocate the PCI bus array dynamically,
  so as not to run off the end of it.
- xserver-1.3.0-mmap-failure-check.patch: Check for failure when mmap'ing
  bus memory. (#234073)
- xserver-1.3.0-rom-search.patch: Look for the sysfs ROM file in the (flat)
  /sys/bus/pci/devices tree, instead of the (bus-topological) /sys/devices,
  so we don't fail to find ROMs merely because they're behind a bridge.
- xserver-1.3.0-no-pseudocolor-composite.patch: Refuse to initialize
  Composite when Render is missing or when the root window is using
  a pseudocolor visual. (#217388)
- xserver-1.3.0-xnest-exposures.patch: Fix Motif app redraw in Xnest. (#229350)

* Fri Apr 06 2007 Adam Jackson <ajax@redhat.com> 1.2.99.905-1
- xserver 1.3 RC5.

* Fri Mar 30 2007 David Woodhouse <dwmw2@redhat.com> 1.2.99.903-2
- Fix regression with PCI domains, but disjoint bus numbers (#207659)

* Fri Mar 30 2007 Adam Jackson <ajax@redhat.com> 1.2.99.903-1
- xserver 1.3 RC3.

* Mon Mar 19 2007 Adam Jackson <ajax@redhat.com> 1.2.99.902-1
- xserver 1.3 RC2.

* Tue Mar 13 2007 Adam Jackson <ajax@redhat.com> 1.2.99.901-2
- xserver-1.2.99.901-xephyr-crash-at-exit.patch: Fix yet another GLX visual
  mess. (#231425)

* Mon Mar 05 2007 Adam Jackson <ajax@redhat.com> 1.2.99.901-1
- xserver 1.3 RC1.  RANDR 1.2 hotness in the hizzouse.
- xserver-1.2.0-honor-displaysize.patch: Honor the DisplaySize config
  directive again (#220248)
- Clean up the post-install cleanup

* Fri Mar 02 2007 Adam Tkac <atkac@redhat.com> 1.2.0-10
- change permissions of files in source package to default from read-only

* Mon Feb 26 2007 Adam Tkac <atkac@redhat.com> 1.2.0-9
- Created new package (xorg-x11-server-source) which is needed to build VNC
  server.

* Fri Feb 23 2007 Adam Jackson <ajax@redhat.com> 1.2.0-8
- xserver-1.2.0-proper-randr-version.patch: Report the RANDR version we
  actually implement, instead of the version defined by the protocol headers.

* Thu Feb 22 2007 Adam Jackson <ajax@redhat.com> 1.2.0-7
- Various backports from git master:
  - xserver-1.2.0-xfixes-clientgone-check.patch: Avoids a crash when sending
    events to clients that just disconnected.
  - xserver-1.2.0-os-memory-leak.patch: Plugs a per-connection memory leak.
  - xserver-1.2.0-int10-rdtsc.patch: Implement rdtsc in the int10 emulator.
  - xserver-1.2.0-glcore-visual-count.patch: Count glcore visuals properly,
    fixes crash at exit.

* Mon Feb 05 2007 Adam Jackson <ajax@redhat.com> 1.2.0-6
- xorg-x11-server-Red-Hat-extramodes.patch:
  - Add 1360x768 normal and reduced-blanking.
  - Add reduced-blanking versions of 1680x1050 and 1920x{1200,1080}.
  - Remove the >60Hz versions of 2560x1600.  Even leaving the 60Hz timing is
    kind of ridiculous, since every real LCD that size I've seen uses the
    reduced blanking timings.  But presumably if you have that nice of a
    monitor, you also have a video card with working DDC.

* Sun Feb 04 2007 Adam Jackson <ajax@redhat.com> 1.2.0-5
- Massive spec formatting and style cleanup.
- Build Xdmx on all arches.
- Enable GL support even on non-DRI machines.
- Re-add DRI to ppc64.
- Update BuildRequires to current versions.
- Remove some bogus Requires.

* Wed Jan 31 2007 Adam Jackson <ajax@redhat.com> 1.2.0-4
- Fix typo in SDK header. (#222487)

* Mon Jan 29 2007 Adam Jackson <ajax@redhat.com> 1.2.0-3
- Fix MMX check on AMD CPUs. (#222332)
- Fix Xephyr keysym init on LP64. (#224311)

* Wed Jan 24 2007 Adam Jackson <ajax@redhat.com> 1.2.0-2
- Delete ModulePath lines rather than attempt to munge them.  (#186338)

* Tue Jan 23 2007 Adam Jackson <ajax@redhat.com> 1.2.0-1
- Xorg server 1.2.0.

* Tue Jan 09 2007 Adam Jackson <ajax@redhat.com> 1.1.1-57
- xorg-xserver-1.1.0-dbe-render.diff: CVE #2006-6101
- xorg-x11-server-1.1.0-redhat-xephyr-only-hack.patch: Skip building the
  non-Xephyr kdrive servers entirely.

* Mon Dec 18 2006 Adam Jackson <ajax@redhat.com> 1.1.1-56
- RHEL5 sync:
  - xorg-x11-server-1.1.1-maxpixclock-option.patch: Allow the maximum pixel
    clock of a monitor to be specified in the config file.
  - xorg-x11-server-1.1.1-glcore-visual-matching.patch: Fix a client crash
    when creating software indirect GLX contexts.
  - xorg-x11-server-1.1.1-vt-activate-is-a-terrible-api.patch: During server
    init, abort if either VT activation ioctl fails.  During shutdown, be
    sure to wait for the VT switch to finish before exiting.

* Mon Dec 11 2006 Adam Jackson <ajax@redhat.com> 1.1.1-55
- xorg-x11-server-1.1.1-lid-close-crash.patch: Added, backport from head.
  (#197921)

* Mon Dec 11 2006 Adam Tkac <atkac redhat com> 1.1.1-54.1.fc7
- fixed building against mesa-6.5.2

* Fri Dec 1 2006 Adam Jackson <ajax@redhat.com> 1.1.1-54.fc7
- xorg-x11-server-1.1.1-xkb-vidmode-switch.patch: Fix string matching on
  XKB actions to be case-insensitive again.  (#216656)

* Fri Dec 1 2006 Adam Jackson <ajax@redhat.com> 1.1.1-53.fc7
- xorg-x11-server-1.1.1-automake-1.10-fixes.patch: Tweak automakefiles to be
  1.10-compliant.
- Misc spec fixes.

* Mon Nov 27 2006 Adam Jackson <ajackson@redhat.com> 1.1.1-52.fc7
- RHEL5 sync:
  - Deliver SecurityPolicy in Xvfb when !with_hw_servers (s390, s390x)
  - xorg-x11-server-1.1.1-ia64-int10.patch: Fix int10 on ia64.
  - xorg-x11-server-1.1.1-ia64-pci-chipsets.patch: ia64 PCI chipset support.
- Unify the autoconfig patches.
- xorg-x11-server-1.1.1-xf86config-comment-less.patch: Added, makes
  pyxf86config not grow the config file every time it's run.
- Remove with_developer_utils macro.

* Fri Nov 10 2006 Adam Jackson <ajackson@redhat.com> 1.1.1-51.fc7
- xorg-x11-server-1.1.1-no-scanpci.patch: Drop scanpci, it's huge and
  there's no added value relative to lspci.
- xorg-x11-server-1.1.1-spurious-libxf1bpp-link.patch: Minor linktime
  fixup.  There's no reason for libxf4bpp to link against libxf1bpp.

* Thu Nov 9 2006 Adam Jackson <ajackson@redhat.com> 1.1.1-50.fc7
- Fix man page globs to not care whether it's .1.gz or .1x.gz, etc.

* Wed Nov 8 2006 Adam Jackson <ajackson@redhat.com> 1.1.1-49.fc7
- Switch to using the x86emu version of libint10 even on x86.  Unifies
  behaviour among CPUs and works around Xen vm86 emulation bogosity.

* Wed Nov 8 2006 Adam Jackson <ajackson@redhat.com>
- Add FC7 todo list
- Bump Release number back to 48, got reduced somehow.

* Fri Oct 13 2006 Kristian Høgsberg <krh@redhat.com> - 1.1.1-48.fc7
- Do not try own /usr/lib/pkgconfig in sdk package.
- Drop dependency on xorg-x11-fonts-base now that we compile in
  'fixed' and 'cursor' fonts.
- Drop xorg-redhat-die-ugly-pattern-die-die-die.patch; use -br option
  instead.

* Wed Oct  4 2006 Soren Sandmann <sandmann@redhat.com> - 1.1.1-47.fc6
- graphics-expose.patch: Call miHandleExposures() with non-translated
  coordinates. 

* Wed Oct  4 2006 Soren Sandmann <sandmann@redhat.com> - 1.1.1-46.fc6
- Fix over-zealous code deletion in graphics-expose.patch. 

* Wed Oct  4 2006 Soren Sandmann <sandmann@redhat.com> - 1.1.1-45.fc6
- xorg-x11-server-1.1.1-graphics-expose.patch: call
  miHandleExposures() in CopyArea/CopyPlane explicitly in cw to
  generate GraphicsExposes correctly. (#209336).

* Mon Oct  2 2006 Kristian Høgsberg <krh@redhat.com> - 1.1.1-44.fc6
- xorg-x11-server-1.1.1-offscreen-pixmaps.patch: Take the server lock
  before calling back into XAA to evict pixmaps (#204810).

* Wed Sep 27 2006 Adam Jackson <ajackson@redhat.com> 1.1.1-43.fc6
- xorg-x11-server-1.1.1-vt-activate-is-a-terrible-api.patch: Since the
  VT_ACTIVATE/VT_WAITACTIVE pair are never guaranteed to successfully
  complete, set a 5 second timeout on the WAITACTIVE, and retry the pair
  until we win.  (#207746)
- xorg-x11-server-1.1.0-pci-scan-fixes.patch: Partial revert to unbreak some
  (but not all) domainful machines, including Pegasos. (#207659)

* Mon Sep 25 2006 Adam Jackson <ajackson@redhat.com> 1.1.1-42.fc6
- xorg-x11-server-1.1.1-getconfig-pl-die-die-die.patch: Fix XGI cards (#208000)

* Fri Sep 22 2006 Adam Jackson <ajackson@redhat.com> 1.1.1-41.fc6
- xorg-x11-server-1.1.1-vbe-filter-less.patch: Be gentler about rejecting
  VESA modes early, since xf86ValidateModes should handle them just fine.

* Wed Sep 20 2006 Adam Jackson <ajackson@redhat.com> 1.1.1-40.fc6
- xorg-x11-server-1.1.1-pclose-confusion.patch: Be sure to call Pclose()
  on pipes created with Popen(), since the additional magic done by Popen()
  relative to popen() is not undone by plain pclose().  (Third base!)
- xorg-x11-server-1.1.1-edid-hex-dump.patch: Backport EDID hex dump code
  from git.

* Wed Sep 20 2006 Kristian Høgsberg <krh@redhat.com> 1.1.1-39.fc6
- Bump xorg-x11-proto-devel BuildRequires version and add Conflict
  line for older mesa releases, so GLX_EXT_texture_from_pixmap opcodes
  match.

* Thu Sep  7 2006 Adam Jackson <ajackson@redhat.coM> - 1.1.1-38.fc6
- xorg-x11-server-1.1.1-believe-monitor-rb-modes.patch: Always believe the
  monitor when it reports a reduced-blanking mode, even over VGA.

* Thu Sep  7 2006 Kristian Høgsberg <krh@redhat.com> - 1.1.1-37.fc6
- Add "built-ins" to default font path.

* Wed Sep  6 2006 Kristian Høgsberg <krh@redhat.com> - 1.1.1-36.fc6
- Enable builtin fallback versions of cursor and fixed fonts.

* Tue Sep  5 2006 Adam Jackson <ajackson@redhat.com> - 1.1.1-35.fc6
- xorg-x11-server-1.1.1-always-mouse-thyself.patch: Fix the check to look
  for mouse/void drivers in the running layout, as opposed to the config file,
  so as not to synthesize two mouse devices.

* Thu Aug 31 2006 Adam Jackson <ajackson@redhat.com> - 1.1.1-34.fc6
- xorg-x11-server-1.1.1-infer-virtual.patch: Be slightly more paranoid about
  setting line pitch, and rescan the mode list after pruning to re-validate
  the estimated virtual size.

* Wed Aug 30 2006 Kristian Høgsberg <krh@redhat.com> - 1.1.1-33.fc6
- Update xorg-x11-server-1.1.1-offscreen-pixmaps.patch to evict pixmap
  when GLX_EXT_texture_from_pixmap is first used.

* Wed Aug 30 2006 Kristian Høgsberg <krh@redhat.com> - 1.1.1-32.fc6
- Drop xorg-x11-server-1.1.0-gl-include-inferiors.patch now that
  compiz can uses the composite overlay window.

* Mon Aug 28 2006 Kristian Høgsberg <krh@redhat.com> - 1.1.1-31.fc6
- Update xorg-x11-server-1.1.1-offscreen-pixmaps.patch to log transitions.
- Update xorg-x11-server-1.1.0-tfp-damage.patch to always bind to
  GL_TEXTURE_RECTANGLE_ARB target.

* Fri Aug 25 2006 Adam Jackson <ajackson@redhat.com> 1.1.1-30.fc6
- xorg-x11-server-1.1.1-pci-paranoia.patch: In xf86MatchPciInstances, fail
  gracefully if xf86PciVideoInfo is NULL (like, on Xen).

* Fri Aug 25 2006 Kristian Høgsberg <krh@redhat.com> - 1.1.1-29.fc6
- Add xorg-x11-server-1.1.1-aiglx-happy-vt-switch.patch to fix VT
  switching (and suspend/resume) when using AIGLX. (#199692, fdo #7916).
- Bump mesa source and libGL BuildRequires.
- Update mesa-6.5.1 patch to work with 6.5.1 rc1 (slang_version_syn.h
  renamed to slang_pp_version_syn.h).

* Thu Aug 24 2006 Adam Jackson <ajackson@redhat.com> - 1.1.1-28.fc6
- xorg-x11-server-1.1.1-infer-virtual.patch: Only flag modes as preferred
  if the EDID block says to.
- xorg-x11-server-1.1.1-mode-sort-kung-fu.patch: Enforce a sort order on
  modes during lookup: builtin before driver before userdef before other,
  and preferred modes within a class before others in that class.

* Tue Aug 22 2006 Adam Jackson <ajackson@redhat.com> - 1.1.1-27.fc6
- xorg-x11-server-1.1.1-edid-quirks-list.patch: Don't set an arbitrary
  pixclock limit if the monitor didn't claim to have one.

* Mon Aug 21 2006 Kristian Høgsberg <krh@redhat.com> - 1.1.1-26.fc6
- Add Tilman Sauerbecks patch to fix AIGLX DRI locking.

* Fri Aug 18 2006 Adam Jackson <ajackson@redhat.com> - 1.1.1-25.fc6
- xorg-x11-server-1.1.1-xvfb-composite-crash.patch: Fix Xvfb's -render flag
  to also disable the Composite extension.
- xorg-x11-server-1.1.1-mesa-6.5.1.patch: Update build system to account for
  Mesa 6.5.1 snapshots.
- xorg-x11-server-1.1.0-edid-mode-injection-2.patch: Add all available
  standard timings from EDID rather than just the first five.

* Fri Aug 18 2006 Adam Jackson <ajackson@redhat.com> - 1.1.1-24.fc6
- xorg-x11-server-1.1.1-edid-quirks-list.patch: Unbreak.

* Fri Aug 18 2006 Adam Jackson <ajackson@redhat.com> - 1.1.1-23.fc6
- xorg-x11-server-1.1.1-xkb-in-xnest.patch: Added. (#193431)

* Thu Aug 17 2006 Adam Jackson <ajackson@redhat.com> - 1.1.1-22.fc6
- xorg-x11-server-1.1.1-infer-virtual.patch: When no modes or virtual size
  are given in the config file, attempt to pick a sensible one by examining
  the EDID modes and physical geometry.  Also generally make the server
  aware of driver-provided modes.
- xorg-x11-server-1.1.1-edid-quirks-list.patch: Redo, since the property I was
  checking for is both fairly common and fairly predictable.  

* Tue Aug 15 2006 Adam Jackson <ajackson@redhat.com> - 1.1.1-21.fc6
- xorg-x11-server-1.1.1-fix-default-mouse-device-yet-again.patch: Added.

* Thu Aug 10 2006 Adam Jackson <ajackson@redhat.com> - 1.1.1-20.fc6
- xorg-x11-server-1.1.1-always-mouse-thyself.patch: If we lack a mouse
  device in the config, and the user hasn't asked for any void devices,
  synthesize a mouse section.  (#200347)
- xorg-x11-server-1.1.1-edid-quirks-list.patch: Better formatting.

* Wed Aug  9 2006 Adam Jackson <ajackson@redhat.com> - 1.1.1-19.fc6
- xorg-x11-server-1.1.1-builderstring.patch: Enable the builder info
  string at configure time;
- ... and use it to print the package name and version.
- xorg-x11-server-1.1.1-defaultdepth-24.patch: Set default depth to 24.
- xorg-x11-server-1.1.1-edid-quirks-list.patch: Add EDID quirks list as
  an experiment; needs a better solution though. 

* Tue Aug  8 2006 Kristian Høgsberg <krh@redhat.com> - 1.1.1-18.fc6
- Update offscreen-pixmaps patch to migrate pixmaps when the compiz
  selection is taken.

* Mon Aug  7 2006 Kristian Høgsberg <krh@redhat.com> - 1.1.1-17.fc5.aiglx
- Build for fc5 aiglx repo.

* Mon Aug  7 2006 Kristian Høgsberg <krh@redhat.com> - 1.1.1-17.fc6
- Add xorg-x11-server-1.1.1-offscreen-pixmaps.patch to default
  XaaNoOffscreenPixmaps to false, for now.

* Mon Aug  7 2006 Adam Jackson <ajackson@redhat.com> 1.1.1-16.fc6
- xorg-x11-server-1.1.0-edid-mode-injection-2.patch: Off-by-one error in
  range storage.

* Wed Aug  2 2006 Adam Jackson <ajackson@redhat.com> 1.1.1-15.fc6
- xorg-x11-server-1.1.0-edid-mode-injection-2.patch: Allow HorizSync and
  VertRefresh to be overridden independently.

* Fri Jul 28 2006 Kevin E Martin <kem@redhat.com> - 1.1.1-14.fc6
- xorg-x11-server-1.1.1-revert-xkb-change.patch: Revert change to xkb that
  broke XkbGetKeyboard().

* Fri Jul 28 2006 Kristian Høgsberg <krh@redhat.com> - 1.1.1-13.fc5.aiglx
- Add conflicts for ABI incompatible version of xorg-x11-drv-i810 and
  xorg-x11-drv-ati.

* Fri Jul 28 2006 Adam Jackson <ajackson@redhat.com> 1.1.1-13.fc6
- Comment out the 848x480 modes from the extramodes patch.  Any panel that
  wants it should be doing EDID injection by now, and it screws up
  autoconfig by _just_ fitting in the ranges for 800x600.

* Wed Jul 26 2006 Mike A. Harris <mharris@redhat.com> 1.1.1-12.fc6
- Added "1920x1080" CVT modes to Red-Hat-extramodes patch for (#195272)
- Sorted the extramodes file by X res, then Y res for ease of maintenance.

* Tue Jul 25 2006 Adam Jackson <ajackson@redhat.com> 1.1.1-11.fc6
- Add selinux{,-devel} buildreqs.

* Tue Jul 25 2006 Adam Jackson <ajackson@redhat.com> 1.1.1-10.fc6
- xorg-x11-server-1.1.1-selinux-awareness.patch: Added for new Mesa
  selinux code.
- xorg-x11-server-1.1.1-Xdmx-render-fix-fdo7482.patch: Backport a Render
  fix for Xdmx.
- xorg-x11-server-1.1.1-no-composite-in-xnest.patch: Disable Composite in
  Xnest, as it's known not to work.
- Fix default font path to match the config file we used to generate.
- Fix default module set to match the config file we used to generate.
- Disable use of TLS GLX dispatch to match Mesa selinux nonsense.

* Mon Jul 24 2006 Mike A. Harris <mharris@redhat.com> 1.1.1-8.fc6
- Added "1440x900@60" CVT mode to Red-Hat-extramodes patch for (#179865)

* Fri Jul 21 2006 Mike A. Harris <mharris@redhat.com>
- Added "1152x864 @ 100.00" GTF mode to Red-Hat-extramodes patch (#49264)

* Fri Jul 21 2006 Mike A. Harris <mharris@redhat.com> 1.1.1-7.fc6
- Only ship pcitweak manpage if we are building it (#199653)
- Fix dist tag usage (Was {dist}, should be {?dist})
- Added xorg-x11-server-libxf86config-dont-write-empty-sections.patch to
  prevent config file parser/writer from writing out empty sections (#198653)
- Add dependency on xorg-x11-fonts-base to all X server subpackages (#186091)

* Tue Jul 18 2006 Jeremy Katz <katzj@redhat.com> 1.1.1-6.fc6
- Saner defaults for hsync/vrefresh on monitors that can't be probed

* Thu Jul 13 2006 Kristian Høgsberg <krh@redhat.com>  1.1.1-5.fc6
- Tag as 1.1.1-5.fc6.

* Wed Jul 12 2006 Kristian Høgsberg <krh@redhat.com>  1.1.1-5.fc5.aiglx
- Enable composite by default.
- Split spiffiffity patch into one patch per change:
  xorg-x11-server-1.1.0-no-move-damage.patch and
  xorg-x11-server-1.1.0-dont-backfill-bg-none.patch.

* Wed Jul 12 2006 Adam Jackson <ajackson@redhat.com> 1.1.1-4.fc6
- Restore placing the raw EDID block on the root window.

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> 1.1.1-3.1.fc6
- rebuild

* Tue Jul 11 2006 Adam Jackson <ajackson@redhat.com> 1.1.1-3.fc6
- Enable DPMS by default.

* Tue Jul 11 2006 Adam Jackson <ajackson@redhat.com> 1.1.1-2.fc6
- Remove nonsensical runtime perl dependency.

* Sat Jul 08 2006 Adam Jackson <ajackson@redhat.com> 1.1.1-1.fc6
- Update to 1.1.1.

* Sat Jul 08 2006 Kristian Høgsberg <krh@redhat.com>  1.1.0-27.fc6
- Enable TLS for GLX to match the mesa build config.

* Fri Jul 07 2006 Kristian Høgsberg <krh@redhat.com>  1.1.0-26
- Add xorg-x11-server-1.1.0-mesa-copy-sub-buffer.patch to hook up the
  GLX_MESA_copy_sub_buffer extension.

* Fri Jun 30 2006 Mike A. Harris <mharris@redhat.com> 1.1.0-25.fc6
- Start using the new %%{dist} tag <http://fedoraproject.org/wiki/DistTag>
  experimentally in the package Release field to help prevent problems like
  (#197266) from occuring in the future.

* Wed Jun 28 2006 Mike A. Harris <mharris@redhat.com>
- Disable build dependency on zlib-devel now that we are not uselessly linking
  against it.

* Tue Jun 27 2006 Adam Jackson <ajackson@redhat.com> 1.1.0-24
- Don't (uselessly) link the server against zlib.
- Fix the 1680x1050 modes to be the CVT timings instead of GTF.

* Mon Jun 26 2006 Adam Jackson <ajackson@redhat.com> 1.1.0-23
- Fix an open-coded check for reduced-blanking modes to only apply to analog
  connectors.
- Reorder the EDID patches slightly.

* Tue Jun 20 2006 Mike A. Harris <mharris@redhat.com> 1.1.0-22
- Added xorg-xserver-1.1.0-setuid.diff to fix potential security issue (#196094)
- Disable DRI on ppc64 builds.
- Conditionalize inclusion of DRI related X server modules to with_dri builds.

* Tue Jun 20 2006 Kristian Høgsberg <krh@redhat.com> 1.1.0-21
- Update xorg-x11-server-1.1.0-tfp-damage.patch to use glTexSubImage2D
  to only update the part of the texture that changed, based on damage
  regions.

* Mon Jun 19 2006 Mike A. Harris <mharris@redhat.com> 1.1.0-20
- Remove with_xnest_server conditional, and fix more BuildRequires to pull
  in libX11-devel, libXext-devel, zlib-devel, etc. for Xnest and Xephyr.
- Remove unwanted files leftover in buildroot for s390/s390x builds.
- Add Xserver.1x manpage to multiple subpackages, as it applies equally to
  Xorg, Xnest, Xvfb, Xephyr.

* Mon Jun 19 2006 Kristian Høgsberg <krh@redhat.com> 1.1.0-19
- Add with_xnest_server conditional and disable on s390, since Xnest
  fails to build on there (Xlib doesn't get added to the link line).
- Add -f to removal of xorgconfig and others which may or may not be built.

* Mon Jun 19 2006 Kristian Høgsberg <krh@redhat.com> 1.1.0-18
- Add xorg-x11-server-1.1.0-convolution-filter-fix.patch and
  xorg-x11-server-1.1.0-tfp-damage.patch backported to make compiz go
  faster and make compiz shadows work.

* Mon Jun 19 2006 Adam Jackson <ajackson@redhat.com> 1.1.0-17
- Disable filling in monitor gamma info from EDID momentarily, since drivers
  will use that field to set the card's gamma ramp.
- Backport some stuff from git: cw crash fix, faster pci scanning, some
  log message cleanup.

* Fri Jun 16 2006 Mike A. Harris <mharris@redhat.com> 1.1.0-16
- Enable spec support for s390, s390x, alpha, sparc, and sparc64 architectures.
- Add with_hw_servers conditional to disable hardware servers on s390/s390x.
- Add with_dmx_server to disable DMX on s390/s390x.
- Added "release" number to "BuildRequires: freetype-devel >= 2.1.9-1" for
  dependency futureproofing.
- Force "--disable-dri" on s390/s390x, to attempt to work around ./configure
  failure to find libdrm, which should not be needed on s390 builds anyway.

* Thu Jun 15 2006 Adam Jackson <ajackson@redhat.com> 1.1.0-15
- Add loader infrastructure for publishing PCI ID lists in the drivers, and
  autodetecting drivers based on that.  Currently unused since no drivers
  publish such a list yet.
- Fix mouse autoconfig to use /dev/input/mice instead of /dev/mouse.

* Wed Jun 14 2006 Kristian Høgsberg <krh@redhat.com> 1.1.0-14
- Change selection atom to _COMPIZ_GL_INCLUDE_INFERIORS in
  xorg-x11-server-1.1.0-gl-include-inferiors.patch.

* Tue Jun 13 2006 Jeremy Katz <katzj@redhat.com> 1.1.0-13
- put back my -fPIC patch, libxf86config isn't built with fPIC otherwise

* Tue Jun 13 2006 Adam Jackson <ajackson@redhat.com> 1.1.0-12
- Add EDID mode autodetection.

* Mon Jun 12 2006 Kristian Høgsberg <krh@redhat.com> 1.1.0-11
- Add xorg-x11-server-1.1.0-gl-include-inferiors.patch to let GL
  rendering include child windows.

* Mon Jun 12 2006 Adam Jackson <ajax@redhat.com> 1.1.0-10
- Misc build fixes for ppc64.

* Mon Jun 12 2006 Adam Jackson <ajax@redhat.com> 1.1.0-9
- --enable-xorg on ppc64 too.
- Re-add cvt, got dropped somehow.

* Fri Jun 09 2006 Kristian Høgsberg <krh@redhat.com> 1.1.0-8
- Add our friend, libtool, to BuildRequires.

* Thu Jun 08 2006 Mike A. Harris <mharris@redhat.com> 1.1.0-7
- Change "BuildRequires: freetype-devel >= 2.1.10" to 2.1.9, as Xorg 7.0
  contains 2.1.9 in "extras" and 7.1 does not appear to have a requirement on
  a newer freetype.
- Janitorial cleanups for spec file changelog consistency.
- Call aclocal before automake, otherwise automake >= 1.9.6 is required in
  order to rebuild the package.
- Build 1.1.0-4, 1.1.0-5, and 1.1.0-6 appear to have failed in brew but nobody
  fixed them.  It appears automake 1.9 breaks the build.

* Wed Jun 07 2006 Jeremy Katz <katzj@redhat.com> 1.1.0-6
- BR automake and autoconf

* Wed Jun 07 2006 Jeremy Katz <katzj@redhat.com> 1.1.0-5
- build on ppc64 so that we have an X server there

* Tue Jun 06 2006 Adam Jackson <ajackson@redhat.com> 1.1.0-4
- Hack the kdrive makefile to only attempt to build Xephyr, avoids linking
  sixteen extra servers just to delete them.
- Move cvt to the default install set, same as gtf.

* Mon Jun 05 2006 Adam Jackson <ajackson@redhat.com> 1.1.0-3
- Drop the libxf86config -fPIC patch, just build the whole thing with
  --with-pic instead.  Add void and evdev to the required driver list for
  upcoming autoconfig magic.

* Thu May 25 2006 Mike A. Harris <mharris@redhat.com> 1.1.0-2
- Add "Requires: xorg-x11-proto-devel >= 7.1-1" to sdk for numerous (52) bug
  reports of drivers failing to build with mock.

* Tue May 23 2006 Adam Jackson <ajackson@redhat.com> 1.1.0-1
- Xorg 7.1 final.

* Tue May 23 2006 Mike A. Harris <mharris@redhat.com> 1.0.99.903-2
- Disable dependency on xorg-x11-drivers package, for OLPC.  (#191781)
- Add "BuildRequires: freetype-devel >= 2.1.10" for bug (#192021)

* Fri May 12 2006 Adam Jackson <ajackson@redhat.com> 1.0.99.903-1
- Update to 7.1RC3, plus experimental fix for fdo bug #6827.

* Mon May 01 2006 Adam Jackson <ajackson@redhat.com> 1.0.99.902-1
- Update to 7.1RC2 plus fix for CVE 2006-1526.  Disable the fastpathing
  patch for fdo bug #4320 since that should be covered in the generic
  Render code now.

* Mon Apr 24 2006 Adam Jackson <ajackson@redhat.com> 1.0.99.901-6
- Backport a Render crash fix from HEAD.

* Thu Apr 13 2006 Kristian Høgsberg <krh@redhat.com> 1.0.99.901-5
- Update spiffiffity patch to only suppress move damage events for
  manually redirected windows.

* Wed Apr 12 2006 Kristian Høgsberg <krh@redhat.com> 1.0.99.901-4
- Bump for rawhide build.

* Wed Apr 12 2006 Kristian Høgsberg <krh@redhat.com> 1.0.99.901-3
- Add xorg-x11-server-1.0.99.901-cow-fix.patch to fix crash when
  releasing the COW.

* Tue Apr 11 2006 Kristian Høgsberg <krh@redhat.com> 1.0.99.901-2
- Bump for fc5 build.

* Sat Apr 08 2006 Adam Jackson <ajackson@redhat.com> 1.0.99.901-1
- Update to 7.1 RC1.

* Thu Apr 06 2006 Adam Jackson <ajax@redhat.com> 1.0.99.2-2
- Remove LBX to match upstream policy.
- Add Xephyr server.

* Tue Apr 04 2006 Kristian Høgsberg <krh@redhat.com> 1.0.99.2-1
- Update to 1.0.99.2 snapshot and go back to using mesa-source package.
- Drop xorg-server-1.0.99-composite-visibility.patch.
- Drop xorg-server-1.0.1-backtrace.patch.
- Drop xorg-server-0.99.3-rgb.txt-dix-config-fix.patch.
- Add xorg-server-1.0.99.2-spiffiffity.patch.

* Thu Mar 23 2006 Kristian Høgsberg <krh@redhat.com>
- Pass --with-dri-driver-path so we're sure to point it to the right path.

* Wed Mar 22 2006 Soren Sandmann <sandmann@redhat.com> 1.0.99.1-2
- Add xorg-server-1.0.99-composite-visibility.patch to get rid of flashing
  titlebars in compositing metacity.

* Tue Mar 21 2006 Kristian Høgsberg <krh@redhat.com> 1.0.99.1-1
- Update to 1.0.99.1 snapshot.

* Mon Mar 06 2006 Jeremy Katz <katzj@redhat.com> 1.0.1-8
- build libxf86config with -fPIC (#181292)
- fix sgi 1600sw extra mode (#182430)

* Wed Feb 22 2006 Jeremy Katz <katzj@redhat.com> 1.0.1-7
- install randrstr.h as part of sdk as required for building some drivers

* Tue Feb 21 2006 Mike A. Harris <mharris@redhat.com>
- Added xorg-server-1.0.1-backtrace.patch which enables the Xorg server's
  built in backtrace support by default, as it was inadvertently disabled in
  7.0.

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> 1.0.1-6.1
- bump again for double-long bug on ppc(64)

* Wed Feb 08 2006 Mike A. Harris <mharris@redhat.com> 1.0.1-6
- Added xorg-x11-server-1.0.1-Red-Hat-extramodes.patch which is a merger of
  XFree86-4.2.99.2-redhat-custom-modelines.patch and
  xorg-x11-6.8.2-laptop-modes.patch from FC4 for (#180301)
- Install a copy of the vesamodes and extramodes files which contain the list
  of video modes that are built into the X server, so that the "rhpxl" package
  does not have to carry around an out of sync copy for itself. (#180301)

* Tue Feb 07 2006 Mike A. Harris <mharris@redhat.com> 1.0.1-5
- Updated "BuildRequires: mesa-source >= 6.4.2-2" to get fix for (#176976)

* Mon Feb 06 2006 Mike A. Harris <mharris@redhat.com> 1.0.1-4
- Fix brown paper bag error introduced in rpm post script in 1.0.1-4.

* Mon Feb 06 2006 Mike A. Harris <mharris@redhat.com> 1.0.1-3
- Added xorg-x11-server-1.0.1-composite-fastpath-fdo4320.patch with changes
  suggested by ajax to fix (fdo#4320).
- Cosmetic cleanups to satiate the banshees.

* Sun Feb 05 2006 Mike A. Harris <mharris@redhat.com> 1.0.1-2
- Added xorg-x11-server-1.0.1-fbpict-fix-rounding.patch from CVS HEAD.
- Added xorg-x11-server-1.0.1-SEGV-on-null-interface.patch which prevents a
  SEGV on null interfaces (#174279,178986)

* Wed Jan 18 2006 Mike A. Harris <mharris@redhat.com> 1.0.1-1
- Updated to xserver 1.0.1 from X11R7.0

* Thu Dec 22 2005 Mike A. Harris <mharris@redhat.com> 1.0.0-3
- Added "Provides: libxf86config-devel = %{version}-%{release}" to sdk package.

* Wed Dec 21 2005 Mike A. Harris <mharris@redhat.com> 1.0.0-2
- Added xserver-1.0.0-parser-add-missing-headers-to-sdk.patch to provide the
  necessary libxf86config.a headers to be able to use the library. (#173084)

* Sat Dec 17 2005 Mike A. Harris <mharris@redhat.com> 1.0.0-1
- Updated to xserver 1.0.0 from X11R7 RC4
- Removed the following patches, which are now integrated upstream:
  - xorg-server-0.99.3-rgb.txt-dix-config-fix.patch,
  - xorg-server-0.99.3-fbmmx-fix-for-non-SSE-cpu.patch
- Changed manNx directories to manN to match upstream defaults.
- Added libxf86config.a to sdk subpackage.
- Updated build dependency of "mesa-libGL-devel >= 6.4.1-1"
- Added "BuildRequires: xorg-x11-font-utils >= 1.0.0-1" to be able to query
  the fontdir from fontutil.pc which is implemented currently by a custom
  patch.
- Enable xtrap, xcsecurity, xevie, and lbx on all builds, not just DRI builds.
- Fix sdk installation path, so that drivers can find the files again.
- Update file manifest, to deal with X server modules that have moved to
  a subdir, etc.

* Mon Nov 28 2005 Kristian Høgsberg <krh@redhat.com>
- Add a few missing BuildRequires.

* Fri Nov 25 2005 Mike A. Harris <mharris@redhat.com> 0.99.2-9
- Added "Requires: xorg-x11-drivers >= 0.99.2-4" as a dependency of the Xorg
  subpackage, to ensure that anaconda installs all of the drivers during OS
  installs and upgrades, as requested by Jeremy Katz.

* Fri Nov 25 2005 Mike A. Harris <mharris@redhat.com> 0.99.2-8
- Added xorg-server-0.99.3-rgb.txt-dix-config-fix.patch which fixes the
  --with-rgb-path option to actually *work*.
- Updated libdrm dep to 1.0.5

* Wed Nov 23 2005 Mike A. Harris <mharris@redhat.com> 0.99.2-7
- Update xorg-x11-server-utils dep to 0.99.2-5 to ensure rgb.txt is installed
  in correct location - _datadir/X11/rgb
- Added --with-rgb-path configure option to specify _datadir/X11/rgb so the
  X server finds the rgb.txt database properly, for bugs (#173453, 173435,
  173428, 173483, 173734, 173737, 173594)
- Added xorg-server-0.99.3-fbmmx-fix-for-non-SSE-cpu.patch to prevent SSE/MMX
  code from being activated on non-capable VIA CPU. (#173384,fdo#5093)

* Thu Nov 17 2005 Mike A. Harris <mharris@redhat.com> 0.99.2-6
- Add the missing rpm pre script from monolithic xorg-x11 packaging,
  clean it up a bit, reorder it for slight performance gain.
- Add some perl magic to pre script to remove RgbPath from xorg.conf,
  in order to fix bug (#173036, 173435, 173453, 173428)
- Add more perl magic to pre script to update ModulePath to the new
  location if it is specified in xorg.conf.
- Added xorg-x11-server-0.99.3-init-origins-fix.patch ported from monolithic
  xorg-x11 package to fix Xinerama bug.
- Added xorg-redhat-die-ugly-pattern-die-die-die.patch to kill the ugly grey
  stipple once again for bug (#173423).
- Added "BuildRequires: libdrm-devel" for DRI enabled builds.

* Mon Nov 14 2005 Jeremy Katz <katzj@redhat.com> 0.99.3-5
- Xorg server should be suid for users to be able to run startx (#173064)

* Mon Nov 14 2005 Mike A. Harris <mharris@redhat.com> 0.99.2-4
- Added temporary "BuildRequires: libXfont-devel >= 0.99.2-3" and
  "Requires: libXfont-devel >= 0.99.2-3" to ensure early-testers of
  pre-rawhide modular X have installed the work around for (#172997).
- Added implementation specific "Requires: xkbdata" to Xorg subpackage, as
  we want to ensure the xkb data files are present, but allow us the option
  of easily switching implementations to "xkeyboard-config" at a future
  date, if we decide to go that route.
- Re-enable _smp_mflags during build.
- Added "Requires: xorg-x11-drv-vesa" to Xorg subpackage (#173060)

* Mon Nov 14 2005 Jeremy Katz <katzj@redhat.com> 0.99.3-3
- provide Xserver
- add another requires for basic bits

* Sun Nov 13 2005 Jeremy Katz <katzj@redhat.com> 0.99.3-2
- add some deps to the Xorg subpackage for base fonts, keyboard and mouse 
  drivers, and rgb.txt that the server really wont work without

* Fri Nov 11 2005 Mike A. Harris <mharris@redhat.com> 0.99.3-1
- Update to xorg-server-0.99.3 from X11R7 RC2.
- Add xorg-server.m4 to sdk subpackage, and "X" symlink to Xorg subpackage.

* Thu Nov 10 2005 Mike A. Harris <mharris@redhat.com> 0.99.2-4
- Added "Requires: xkbcomp" for Xorg server, as it invokes it internally.

* Wed Nov 09 2005 Mike A. Harris <mharris@redhat.com> 0.99.2-3
- Added "BuildRequires: libXtst-devel" for Xtst examples.

* Mon Nov 07 2005 Mike A. Harris <mharris@redhat.com> 0.99.2-2
- Added versioning to Xorg virtual Provide, to allow config tools and driver
  packages to have version based requires.

* Thu Oct 27 2005 Mike A. Harris <mharris@redhat.com> 0.99.2-1
- Update to xorg-server-0.99.2 from X11R7 RC1.
- Add "BuildRequires: xorg-x11-util-macros >= 0.99.1".
- Add "BuildRequires: mesa-source >= 6.4-4" for DRI builds.
- Added dmx related utilities to Xdmx subpackage.
- Individually list each X server module in file manifest.
- Hack man1 manpages to be installed into man1x.
- Add the following ./configure options --disable-dependency-tracking,
  --enable-composite, --enable-xtrap, --enable-xcsecurity, --enable-xevie,
  --enable-lbx, --enable-dri, --with-mesa-source, --with-module-dir,
  --with-os-name, --with-os-vendor, --with-xkb-output, --disable-xorgcfg
- Added getconfig, scanpci et al to Xorg subpackage
- Added inb, inl, inw, ioport, outboutl, outw, pcitweak utils to Xorg package
  conditionally, defaulting to "off".  These utilities are potentially
  dangerous and can physically damage hardware and/or destroy data, so are
  not shipped by default.
- Added "BuildRequires: libdmx-devel" for dmx utilities
- Added "BuildRequires: libXres-devel" for Xres examples
- Added {_libdir}/xserver/SecurityPolicy to Xorg subpackage for XSECURITY

* Mon Oct 03 2005 Mike A. Harris <mharris@redhat.com> 0.99.1-2.cvs20050830.2
- Fix license tag to be "MIT/X11"
- Change Xdmx subpackage to Obsolete xorg-x11-Xdmx instead of xorg-x11-Xnest

* Sun Oct 02 2005 Mike A. Harris <mharris@redhat.com> 0.99.1-2.cvs20050830.1
- Update BuildRequires for new library package naming (libX...)
- Use Fedora Extras style BuildRoot tag
- Invoke make with _smp_mflags to take advantage of SMP systems

* Tue Aug 30 2005 Kristian Hogsberg <krh@redhat.com> 0.99.1-2.cvs20050830
- Go back to %spec -n, use new cvs snapshot that supports overriding
  moduledir during make install, use %makeinstall.
- Drop %{moduledir}/multimedia globs.

* Fri Aug 26 2005 Mike A. Harris <mharris@redhat.com> 0.99.1-2.cvs20050825.0
- Added build dependency on xorg-x11-libfontenc-devel, as the build fails
  half way through without it, even though upstream dependencies do not
  specify it as required.

* Tue Aug 23 2005 Kristian Hogsberg <krh@redhat.com> 0.99.1-1
- Initial spec file for the modular X server.
