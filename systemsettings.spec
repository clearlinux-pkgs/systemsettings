#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v4
# autospec commit: a166baf
#
# Source0 file verified with key 0xD7574483BB57B18D (jr@jriddell.org)
#
Name     : systemsettings
Version  : 6.0.2
Release  : 90
URL      : https://download.kde.org/stable/plasma/6.0.2/systemsettings-6.0.2.tar.xz
Source0  : https://download.kde.org/stable/plasma/6.0.2/systemsettings-6.0.2.tar.xz
Source1  : https://download.kde.org/stable/plasma/6.0.2/systemsettings-6.0.2.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause CC0-1.0 GPL-2.0 GPL-3.0 LGPL-2.0 LGPL-2.1
Requires: systemsettings-bin = %{version}-%{release}
Requires: systemsettings-data = %{version}-%{release}
Requires: systemsettings-lib = %{version}-%{release}
Requires: systemsettings-license = %{version}-%{release}
Requires: systemsettings-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : kcmutils-dev
BuildRequires : kio-dev
BuildRequires : kirigami-dev
BuildRequires : krunner-dev
BuildRequires : plasma-activities-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
No detailed description available

%package bin
Summary: bin components for the systemsettings package.
Group: Binaries
Requires: systemsettings-data = %{version}-%{release}
Requires: systemsettings-license = %{version}-%{release}

%description bin
bin components for the systemsettings package.


%package data
Summary: data components for the systemsettings package.
Group: Data

%description data
data components for the systemsettings package.


%package doc
Summary: doc components for the systemsettings package.
Group: Documentation

%description doc
doc components for the systemsettings package.


%package lib
Summary: lib components for the systemsettings package.
Group: Libraries
Requires: systemsettings-data = %{version}-%{release}
Requires: systemsettings-license = %{version}-%{release}

%description lib
lib components for the systemsettings package.


%package license
Summary: license components for the systemsettings package.
Group: Default

%description license
license components for the systemsettings package.


%package locales
Summary: locales components for the systemsettings package.
Group: Default

%description locales
locales components for the systemsettings package.


%prep
%setup -q -n systemsettings-6.0.2
cd %{_builddir}/systemsettings-6.0.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1710348572
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake ..
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1710348572
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/systemsettings
cp %{_builddir}/systemsettings-%{version}/LICENSES/BSD-2-Clause.txt %{buildroot}/usr/share/package-licenses/systemsettings/ea97eb88ae53ec41e26f8542176ab986d7bc943a || :
cp %{_builddir}/systemsettings-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/systemsettings/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0 || :
cp %{_builddir}/systemsettings-%{version}/LICENSES/GPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/systemsettings/3e8971c6c5f16674958913a94a36b1ea7a00ac46 || :
cp %{_builddir}/systemsettings-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/systemsettings/3e8971c6c5f16674958913a94a36b1ea7a00ac46 || :
cp %{_builddir}/systemsettings-%{version}/LICENSES/GPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/systemsettings/2123756e0b1fc8243547235a33c0fcabfe3b9a51 || :
cp %{_builddir}/systemsettings-%{version}/LICENSES/LGPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/systemsettings/a4c60b3fefda228cd7439d3565df043192fef137 || :
cp %{_builddir}/systemsettings-%{version}/LICENSES/LGPL-2.1-or-later.txt %{buildroot}/usr/share/package-licenses/systemsettings/fa05e58320cb7c64786b26396f4b992579a628bc || :
cp %{_builddir}/systemsettings-%{version}/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/systemsettings/7d9831e05094ce723947d729c2a46a09d6e90275 || :
cp %{_builddir}/systemsettings-%{version}/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/systemsettings/7d9831e05094ce723947d729c2a46a09d6e90275 || :
cp %{_builddir}/systemsettings-%{version}/runner/systemsettingsrunner.json.license %{buildroot}/usr/share/package-licenses/systemsettings/fd32940f125ecf08f9ad3cb0b64251688e927a90 || :
export GOAMD64=v2
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
%find_lang systemsettings
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/systemsettings
/usr/bin/systemsettings

%files data
%defattr(-,root,root,-)
/usr/share/applications/kdesystemsettings.desktop
/usr/share/applications/systemsettings.desktop
/usr/share/kglobalaccel/systemsettings.desktop
/usr/share/metainfo/org.kde.systemsettings.metainfo.xml
/usr/share/qlogging-categories6/systemsettings.categories
/usr/share/systemsettings/categories/settings-appearance-font.desktop
/usr/share/systemsettings/categories/settings-appearance-themes.desktop
/usr/share/systemsettings/categories/settings-appearance.desktop
/usr/share/systemsettings/categories/settings-applications-defaults.desktop
/usr/share/systemsettings/categories/settings-applications-permissions.desktop
/usr/share/systemsettings/categories/settings-applications.desktop
/usr/share/systemsettings/categories/settings-hardware-display.desktop
/usr/share/systemsettings/categories/settings-hardware-input-pointing-devices.desktop
/usr/share/systemsettings/categories/settings-hardware-input-touchscreen.desktop
/usr/share/systemsettings/categories/settings-hardware-input.desktop
/usr/share/systemsettings/categories/settings-hardware-keyboard.desktop
/usr/share/systemsettings/categories/settings-hardware-multimedia.desktop
/usr/share/systemsettings/categories/settings-hardware-removable-storage.desktop
/usr/share/systemsettings/categories/settings-hardware.desktop
/usr/share/systemsettings/categories/settings-network-networksettings.desktop
/usr/share/systemsettings/categories/settings-network.desktop
/usr/share/systemsettings/categories/settings-personalization.desktop
/usr/share/systemsettings/categories/settings-regionalsettings.desktop
/usr/share/systemsettings/categories/settings-root-category.desktop
/usr/share/systemsettings/categories/settings-security-privacy.desktop
/usr/share/systemsettings/categories/settings-system-administration.desktop
/usr/share/systemsettings/categories/settings-workspace-search.desktop
/usr/share/systemsettings/categories/settings-workspace-session.desktop
/usr/share/systemsettings/categories/settings-workspace-windowmanagement.desktop
/usr/share/systemsettings/categories/settings-workspace.desktop
/usr/share/zsh/site-functions/_systemsettings

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/ca/systemsettings/index.cache.bz2
/usr/share/doc/HTML/ca/systemsettings/index.docbook
/usr/share/doc/HTML/de/systemsettings/index.cache.bz2
/usr/share/doc/HTML/de/systemsettings/index.docbook
/usr/share/doc/HTML/en/systemsettings/index.cache.bz2
/usr/share/doc/HTML/en/systemsettings/index.docbook
/usr/share/doc/HTML/es/systemsettings/index.cache.bz2
/usr/share/doc/HTML/es/systemsettings/index.docbook
/usr/share/doc/HTML/fr/systemsettings/index.cache.bz2
/usr/share/doc/HTML/fr/systemsettings/index.docbook
/usr/share/doc/HTML/id/systemsettings/index.cache.bz2
/usr/share/doc/HTML/id/systemsettings/index.docbook
/usr/share/doc/HTML/it/systemsettings/index.cache.bz2
/usr/share/doc/HTML/it/systemsettings/index.docbook
/usr/share/doc/HTML/nl/systemsettings/index.cache.bz2
/usr/share/doc/HTML/nl/systemsettings/index.docbook
/usr/share/doc/HTML/pt/systemsettings/index.cache.bz2
/usr/share/doc/HTML/pt/systemsettings/index.docbook
/usr/share/doc/HTML/pt_BR/systemsettings/index.cache.bz2
/usr/share/doc/HTML/pt_BR/systemsettings/index.docbook
/usr/share/doc/HTML/ru/systemsettings/index.cache.bz2
/usr/share/doc/HTML/ru/systemsettings/index.docbook
/usr/share/doc/HTML/sv/systemsettings/index.cache.bz2
/usr/share/doc/HTML/sv/systemsettings/index.docbook
/usr/share/doc/HTML/tr/systemsettings/index.cache.bz2
/usr/share/doc/HTML/tr/systemsettings/index.docbook
/usr/share/doc/HTML/uk/systemsettings/index.cache.bz2
/usr/share/doc/HTML/uk/systemsettings/index.docbook

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libsystemsettingsview.so.3
/V3/usr/lib64/qt6/plugins/kf6/krunner/krunner_systemsettings.so
/usr/lib64/libsystemsettingsview.so.3
/usr/lib64/qt6/plugins/kf6/krunner/krunner_systemsettings.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/systemsettings/2123756e0b1fc8243547235a33c0fcabfe3b9a51
/usr/share/package-licenses/systemsettings/3e8971c6c5f16674958913a94a36b1ea7a00ac46
/usr/share/package-licenses/systemsettings/7d9831e05094ce723947d729c2a46a09d6e90275
/usr/share/package-licenses/systemsettings/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
/usr/share/package-licenses/systemsettings/a4c60b3fefda228cd7439d3565df043192fef137
/usr/share/package-licenses/systemsettings/ea97eb88ae53ec41e26f8542176ab986d7bc943a
/usr/share/package-licenses/systemsettings/fa05e58320cb7c64786b26396f4b992579a628bc
/usr/share/package-licenses/systemsettings/fd32940f125ecf08f9ad3cb0b64251688e927a90

%files locales -f systemsettings.lang
%defattr(-,root,root,-)

