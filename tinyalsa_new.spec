Summary: Tinyalsa Library
Name: tinyalsa_new
Version: 1.0
Release: r0
License: BSD-3-Clause
URL: https://github.com/tinyalsa/tinyalsa
Source0: %{name}-%{version}.tar.gz

BuildRequires: cmake libtool gcc-g++ systemd-rpm-macros libcutils
Requires: libcutils, libtool


%description
This is the tinyalsa library, it provides pcm and mixer interfaces to
client for various audio playback and capture use cases.


%package -n tinyalsa_new-devel
Summary: Tinyalsa Library - Development files
License: BSD-3-Clause

%description -n tinyalsa_new-devel
This is the tinyalsa library, it provides pcm and mixer interfaces to
client for various audio playback and capture use cases.  This package
contains symbolic links, header files, and related items necessary for
software development.

%global debug_package %{nil}
%global __os_install_post %{nil}

%prep
%autosetup -n %{name}-%{version}

%build
%cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_TOOLCHAIN_FILE=$CMAKE_TOOLCHAIN_FILE -DCMAKE_RULE_MESSAGES:BOOL=OFF -DCMAKE_VERBOSE_MAKEFILE:BOOL=$VER -DCMAKE_INSTALL_INCLUDEDIR=%{_includedir} -DCMAKE_INSTALL_LIBDIR=%{_libdir} -DCMAKE_INSTALL_BINDIR=%{_bindir} -DCMAKE_INSTALL_LICENSEDIR=%{_defaultlicensedir}
%cmake_build

%install
%cmake_install

%files

%{_bindir}/tinyplay
%{_bindir}/tinycap
%{_bindir}/tinypcminfo
%{_bindir}/tinymix
%{_bindir}/tinywavinfo
%{_libdir}/libtinyalsa.so.2.0.0
%{_libdir}/libtinyalsa.so.2

%files -n tinyalsa_new-devel
%{_includedir}/tinyalsa/attributes.h
%{_includedir}/tinyalsa/version.h
%{_includedir}/tinyalsa/asoundlib.h
%{_includedir}/tinyalsa/pcm.h
%{_includedir}/tinyalsa/plugin.h
%{_includedir}/tinyalsa/mixer.h
%{_libdir}/libtinyalsa.so
