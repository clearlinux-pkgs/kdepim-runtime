#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v2
# autospec commit: e661f3a
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : kdepim-runtime
Version  : 23.08.3
Release  : 65
URL      : https://download.kde.org/stable/release-service/23.08.3/src/kdepim-runtime-23.08.3.tar.xz
Source0  : https://download.kde.org/stable/release-service/23.08.3/src/kdepim-runtime-23.08.3.tar.xz
Source1  : https://download.kde.org/stable/release-service/23.08.3/src/kdepim-runtime-23.08.3.tar.xz.sig
Summary  : Extends the functionality of kdepim
Group    : Development/Tools
License  : AGPL-3.0 BSD-2-Clause BSD-3-Clause CC0-1.0 GPL-2.0 GPL-3.0 LGPL-2.0 LGPL-2.1 LGPL-3.0
Requires: kdepim-runtime-bin = %{version}-%{release}
Requires: kdepim-runtime-data = %{version}-%{release}
Requires: kdepim-runtime-lib = %{version}-%{release}
Requires: kdepim-runtime-license = %{version}-%{release}
Requires: kdepim-runtime-locales = %{version}-%{release}
BuildRequires : akonadi-calendar-dev
BuildRequires : akonadi-contacts-dev
BuildRequires : akonadi-dev
BuildRequires : akonadi-mime-dev
BuildRequires : akonadi-notes-dev
BuildRequires : boost-dev
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules pkgconfig(libsasl2)
BuildRequires : extra-cmake-modules shared-mime-info
BuildRequires : extra-cmake-modules-data
BuildRequires : grantlee-dev
BuildRequires : grantleetheme-dev
BuildRequires : kcalendarcore-dev
BuildRequires : kcalutils-dev
BuildRequires : kcontacts-dev
BuildRequires : kdav-dev
BuildRequires : kholidays-dev
BuildRequires : kidentitymanagement-dev
BuildRequires : kimap-staticdev
BuildRequires : kldap-dev
BuildRequires : kmailtransport-dev
BuildRequires : kmbox-dev
BuildRequires : kmime-dev
BuildRequires : knotifyconfig-dev
BuildRequires : kpimtextedit-dev
BuildRequires : libkdepim-dev
BuildRequires : libkgapi-dev
BuildRequires : pimcommon-dev
BuildRequires : pkgconfig(libsecret-1)
BuildRequires : qca-qt5-dev
BuildRequires : qtbase-dev mesa-dev
BuildRequires : qtwebengine-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
The KDE project kdepim-runtime contains the Akonadi resources from kdepim which can be used without the applications in kdepim.

%package bin
Summary: bin components for the kdepim-runtime package.
Group: Binaries
Requires: kdepim-runtime-data = %{version}-%{release}
Requires: kdepim-runtime-license = %{version}-%{release}

%description bin
bin components for the kdepim-runtime package.


%package data
Summary: data components for the kdepim-runtime package.
Group: Data

%description data
data components for the kdepim-runtime package.


%package doc
Summary: doc components for the kdepim-runtime package.
Group: Documentation

%description doc
doc components for the kdepim-runtime package.


%package lib
Summary: lib components for the kdepim-runtime package.
Group: Libraries
Requires: kdepim-runtime-data = %{version}-%{release}
Requires: kdepim-runtime-license = %{version}-%{release}

%description lib
lib components for the kdepim-runtime package.


%package license
Summary: license components for the kdepim-runtime package.
Group: Default

%description license
license components for the kdepim-runtime package.


%package locales
Summary: locales components for the kdepim-runtime package.
Group: Default

%description locales
locales components for the kdepim-runtime package.


%prep
%setup -q -n kdepim-runtime-23.08.3
cd %{_builddir}/kdepim-runtime-23.08.3

%build
## build_prepend content
# Make sure the package only builds if kalarmcal has been updated first
sed -i -r -e 's,(KF.?AlarmCalendar \$\{AKONADIKALARM_LIB_VERSION\} CONFIG)(.*\)),\1 REQUIRED \2,' CMakeLists.txt || :
## build_prepend end
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1699916675
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
%cmake ..
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
## build_prepend content
# Make sure the package only builds if kalarmcal has been updated first
sed -i -r -e 's,(KF.?AlarmCalendar \$\{AKONADIKALARM_LIB_VERSION\} CONFIG)(.*\)),\1 REQUIRED \2,' CMakeLists.txt || :
## build_prepend end
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
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
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
export SOURCE_DATE_EPOCH=1699916675
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kdepim-runtime
cp %{_builddir}/kdepim-runtime-%{version}/LICENSES/AGPL-3.0-or-later.txt %{buildroot}/usr/share/package-licenses/kdepim-runtime/971f2a85c02441da0d59ff0790511592a0114532 || :
cp %{_builddir}/kdepim-runtime-%{version}/LICENSES/BSD-2-Clause.txt %{buildroot}/usr/share/package-licenses/kdepim-runtime/680ed9349d3d12bd39ddd36e8c4bc6b1b0cb1c0e || :
cp %{_builddir}/kdepim-runtime-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/kdepim-runtime/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c || :
cp %{_builddir}/kdepim-runtime-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/kdepim-runtime/8287b608d3fa40ef401339fd907ca1260c964123 || :
cp %{_builddir}/kdepim-runtime-%{version}/LICENSES/GPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/kdepim-runtime/2a638514c87c4923c0570c55822620fad56f2a33 || :
cp %{_builddir}/kdepim-runtime-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kdepim-runtime/e712eadfab0d2357c0f50f599ef35ee0d87534cb || :
cp %{_builddir}/kdepim-runtime-%{version}/LICENSES/GPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/kdepim-runtime/6091db0aead0d90182b93d3c0d09ba93d188f907 || :
cp %{_builddir}/kdepim-runtime-%{version}/LICENSES/GPL-3.0-or-later.txt %{buildroot}/usr/share/package-licenses/kdepim-runtime/6091db0aead0d90182b93d3c0d09ba93d188f907 || :
cp %{_builddir}/kdepim-runtime-%{version}/LICENSES/LGPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/kdepim-runtime/20079e8f79713dce80ab09774505773c926afa2a || :
cp %{_builddir}/kdepim-runtime-%{version}/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kdepim-runtime/20079e8f79713dce80ab09774505773c926afa2a || :
cp %{_builddir}/kdepim-runtime-%{version}/LICENSES/LGPL-2.1-or-later.txt %{buildroot}/usr/share/package-licenses/kdepim-runtime/6f1f675aa5f6a2bbaa573b8343044b166be28399 || :
cp %{_builddir}/kdepim-runtime-%{version}/LICENSES/LGPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/kdepim-runtime/757b86330df80f81143d5916b3e92b4bcb1b1890 || :
cp %{_builddir}/kdepim-runtime-%{version}/LICENSES/LGPL-3.0-or-later.txt %{buildroot}/usr/share/package-licenses/kdepim-runtime/757b86330df80f81143d5916b3e92b4bcb1b1890 || :
cp %{_builddir}/kdepim-runtime-%{version}/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/kdepim-runtime/7d9831e05094ce723947d729c2a46a09d6e90275 || :
cp %{_builddir}/kdepim-runtime-%{version}/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/kdepim-runtime/7d9831e05094ce723947d729c2a46a09d6e90275 || :
cp %{_builddir}/kdepim-runtime-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/kdepim-runtime/e458941548e0864907e654fa2e192844ae90fc32 || :
cp %{_builddir}/kdepim-runtime-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/kdepim-runtime/e458941548e0864907e654fa2e192844ae90fc32 || :
pushd clr-build-avx2
%make_install_v3  || :
popd
pushd clr-build
%make_install
popd
%find_lang accountwizard_contacts
%find_lang accountwizard_ews
%find_lang accountwizard_ical
%find_lang accountwizard_imap
%find_lang accountwizard_kolab
%find_lang accountwizard_mailbox
%find_lang accountwizard_maildir
%find_lang accountwizard_pop3
%find_lang accountwizard_vcard
%find_lang accountwizard_vcarddir
%find_lang akonadi-filestore
%find_lang akonadi_birthdays_resource
%find_lang akonadi_contacts_resource
%find_lang akonadi_davgroupware_resource
%find_lang akonadi_etesync_resource
%find_lang akonadi_ews_resource
%find_lang akonadi_google_resource
%find_lang akonadi_ical_resource
%find_lang akonadi_icaldir_resource
%find_lang akonadi_imap_resource
%find_lang akonadi_maildir_resource
%find_lang akonadi_maildispatcher_agent
%find_lang akonadi_mbox_resource
%find_lang akonadi_migration_agent
%find_lang akonadi_mixedmaildir_resource
%find_lang akonadi_newmailnotifier_agent
%find_lang akonadi_openxchange_resource
%find_lang akonadi_pop3_resource
%find_lang akonadi_singlefile_resource
%find_lang akonadi_tomboynotes_resource
%find_lang akonadi_vcard_resource
%find_lang akonadi_vcarddir_resource
%find_lang gid-migrator
%find_lang kio_akonadi
%find_lang libfolderarchivesettings
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/akonadi_akonotes_resource
/V3/usr/bin/akonadi_birthdays_resource
/V3/usr/bin/akonadi_contacts_resource
/V3/usr/bin/akonadi_davgroupware_resource
/V3/usr/bin/akonadi_ews_resource
/V3/usr/bin/akonadi_ewsmta_resource
/V3/usr/bin/akonadi_google_resource
/V3/usr/bin/akonadi_ical_resource
/V3/usr/bin/akonadi_icaldir_resource
/V3/usr/bin/akonadi_imap_resource
/V3/usr/bin/akonadi_maildir_resource
/V3/usr/bin/akonadi_maildispatcher_agent
/V3/usr/bin/akonadi_mbox_resource
/V3/usr/bin/akonadi_migration_agent
/V3/usr/bin/akonadi_mixedmaildir_resource
/V3/usr/bin/akonadi_newmailnotifier_agent
/V3/usr/bin/akonadi_notes_resource
/V3/usr/bin/akonadi_openxchange_resource
/V3/usr/bin/akonadi_pop3_resource
/V3/usr/bin/akonadi_tomboynotes_resource
/V3/usr/bin/akonadi_vcard_resource
/V3/usr/bin/akonadi_vcarddir_resource
/V3/usr/bin/gidmigrator
/usr/bin/akonadi_akonotes_resource
/usr/bin/akonadi_birthdays_resource
/usr/bin/akonadi_contacts_resource
/usr/bin/akonadi_davgroupware_resource
/usr/bin/akonadi_ews_resource
/usr/bin/akonadi_ewsmta_resource
/usr/bin/akonadi_google_resource
/usr/bin/akonadi_ical_resource
/usr/bin/akonadi_icaldir_resource
/usr/bin/akonadi_imap_resource
/usr/bin/akonadi_maildir_resource
/usr/bin/akonadi_maildispatcher_agent
/usr/bin/akonadi_mbox_resource
/usr/bin/akonadi_migration_agent
/usr/bin/akonadi_mixedmaildir_resource
/usr/bin/akonadi_newmailnotifier_agent
/usr/bin/akonadi_notes_resource
/usr/bin/akonadi_openxchange_resource
/usr/bin/akonadi_pop3_resource
/usr/bin/akonadi_tomboynotes_resource
/usr/bin/akonadi_vcard_resource
/usr/bin/akonadi_vcarddir_resource
/usr/bin/gidmigrator

%files data
%defattr(-,root,root,-)
/usr/share/akonadi/accountwizard/contacts/contactswizard.desktop
/usr/share/akonadi/accountwizard/contacts/contactswizard.es
/usr/share/akonadi/accountwizard/contacts/contactswizard.ui
/usr/share/akonadi/accountwizard/ical/icalwizard.desktop
/usr/share/akonadi/accountwizard/ical/icalwizard.es
/usr/share/akonadi/accountwizard/ical/icalwizard.ui
/usr/share/akonadi/accountwizard/imap/imapwizard.desktop
/usr/share/akonadi/accountwizard/imap/imapwizard.es
/usr/share/akonadi/accountwizard/imap/imapwizard.ui
/usr/share/akonadi/accountwizard/mailbox/mailboxwizard.desktop
/usr/share/akonadi/accountwizard/mailbox/mailboxwizard.es
/usr/share/akonadi/accountwizard/mailbox/mailboxwizard.ui
/usr/share/akonadi/accountwizard/maildir/maildirwizard.desktop
/usr/share/akonadi/accountwizard/maildir/maildirwizard.es
/usr/share/akonadi/accountwizard/maildir/maildirwizard.ui
/usr/share/akonadi/accountwizard/pop3/pop3wizard.desktop
/usr/share/akonadi/accountwizard/pop3/pop3wizard.es
/usr/share/akonadi/accountwizard/pop3/pop3wizard.ui
/usr/share/akonadi/accountwizard/vcard/vcardwizard.desktop
/usr/share/akonadi/accountwizard/vcard/vcardwizard.es
/usr/share/akonadi/accountwizard/vcard/vcardwizard.ui
/usr/share/akonadi/accountwizard/vcarddir/vcarddirwizard.desktop
/usr/share/akonadi/accountwizard/vcarddir/vcarddirwizard.es
/usr/share/akonadi/accountwizard/vcarddir/vcarddirwizard.ui
/usr/share/akonadi/agents/akonotesresource.desktop
/usr/share/akonadi/agents/birthdaysresource.desktop
/usr/share/akonadi/agents/contactsresource.desktop
/usr/share/akonadi/agents/davgroupwareresource.desktop
/usr/share/akonadi/agents/ewsmtaresource.desktop
/usr/share/akonadi/agents/ewsresource.desktop
/usr/share/akonadi/agents/googleresource.desktop
/usr/share/akonadi/agents/icaldirresource.desktop
/usr/share/akonadi/agents/icalresource.desktop
/usr/share/akonadi/agents/imapresource.desktop
/usr/share/akonadi/agents/maildirresource.desktop
/usr/share/akonadi/agents/maildispatcheragent.desktop
/usr/share/akonadi/agents/mboxresource.desktop
/usr/share/akonadi/agents/migrationagent.desktop
/usr/share/akonadi/agents/mixedmaildirresource.desktop
/usr/share/akonadi/agents/newmailnotifieragent.desktop
/usr/share/akonadi/agents/notesresource.desktop
/usr/share/akonadi/agents/openxchangeresource.desktop
/usr/share/akonadi/agents/pop3resource.desktop
/usr/share/akonadi/agents/tomboynotesresource.desktop
/usr/share/akonadi/agents/vcarddirresource.desktop
/usr/share/akonadi/agents/vcardresource.desktop
/usr/share/akonadi/firstrun/birthdaycalendar
/usr/share/akonadi/firstrun/defaultaddressbook
/usr/share/akonadi/firstrun/defaultcalendar
/usr/share/akonadi/firstrun/defaultnotebook
/usr/share/applications/org.kde.akonadi_contacts_resource.desktop
/usr/share/applications/org.kde.akonadi_davgroupware_resource.desktop
/usr/share/applications/org.kde.akonadi_ews_resource.desktop
/usr/share/applications/org.kde.akonadi_google_resource.desktop
/usr/share/applications/org.kde.akonadi_imap_resource.desktop
/usr/share/applications/org.kde.akonadi_openxchange_resource.desktop
/usr/share/applications/org.kde.akonadi_vcard_resource.desktop
/usr/share/applications/org.kde.akonadi_vcarddir_resource.desktop
/usr/share/dbus-1/interfaces/org.kde.Akonadi.Maildir.Settings.xml
/usr/share/dbus-1/interfaces/org.kde.Akonadi.MixedMaildir.Settings.xml
/usr/share/icons/hicolor/128x128/apps/akonadi-ews.png
/usr/share/icons/hicolor/128x128/apps/ox.png
/usr/share/icons/hicolor/16x16/apps/akonadi-ews.png
/usr/share/icons/hicolor/16x16/apps/ox.png
/usr/share/icons/hicolor/22x22/apps/akonadi-ews.png
/usr/share/icons/hicolor/24x24/apps/akonadi-ews.png
/usr/share/icons/hicolor/32x32/apps/akonadi-ews.png
/usr/share/icons/hicolor/32x32/apps/ox.png
/usr/share/icons/hicolor/48x48/apps/akonadi-ews.png
/usr/share/icons/hicolor/48x48/apps/ox.png
/usr/share/icons/hicolor/64x64/apps/akonadi-ews.png
/usr/share/icons/hicolor/64x64/apps/ox.png
/usr/share/icons/hicolor/72x72/apps/akonadi-ews.png
/usr/share/icons/hicolor/96x96/apps/akonadi-ews.png
/usr/share/knotifications5/akonadi_ews_resource.notifyrc
/usr/share/knotifications5/akonadi_google_resource.notifyrc
/usr/share/knotifications5/akonadi_maildispatcher_agent.notifyrc
/usr/share/knotifications5/akonadi_newmailnotifier_agent.notifyrc
/usr/share/knotifications5/akonadi_pop3_resource.notifyrc
/usr/share/kservices5/akonadi/davgroupware-providers/citadel.desktop
/usr/share/kservices5/akonadi/davgroupware-providers/davical.desktop
/usr/share/kservices5/akonadi/davgroupware-providers/egroupware.desktop
/usr/share/kservices5/akonadi/davgroupware-providers/mailbox-org.desktop
/usr/share/kservices5/akonadi/davgroupware-providers/nextcloud.desktop
/usr/share/kservices5/akonadi/davgroupware-providers/opengroupware.desktop
/usr/share/kservices5/akonadi/davgroupware-providers/owncloud-pre5.desktop
/usr/share/kservices5/akonadi/davgroupware-providers/owncloud-pre9.desktop
/usr/share/kservices5/akonadi/davgroupware-providers/owncloud.desktop
/usr/share/kservices5/akonadi/davgroupware-providers/scalix.desktop
/usr/share/kservices5/akonadi/davgroupware-providers/sogo.desktop
/usr/share/kservices5/akonadi/davgroupware-providers/yahoo.desktop
/usr/share/kservices5/akonadi/davgroupware-providers/zarafa.desktop
/usr/share/kservices5/akonadi/davgroupware-providers/zimbra.desktop
/usr/share/mime-packages/kdepim-mime.xml
/usr/share/qlogging-categories5/kdepim-runtime.categories
/usr/share/qlogging-categories5/kdepim-runtime.renamecategories

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/ca/kioslave5/pop3/index.cache.bz2
/usr/share/doc/HTML/ca/kioslave5/pop3/index.docbook
/usr/share/doc/HTML/de/kioslave5/pop3/index.cache.bz2
/usr/share/doc/HTML/de/kioslave5/pop3/index.docbook
/usr/share/doc/HTML/en/kioslave5/pop3/index.cache.bz2
/usr/share/doc/HTML/en/kioslave5/pop3/index.docbook
/usr/share/doc/HTML/es/kioslave5/pop3/index.cache.bz2
/usr/share/doc/HTML/es/kioslave5/pop3/index.docbook
/usr/share/doc/HTML/et/kioslave5/pop3/index.cache.bz2
/usr/share/doc/HTML/et/kioslave5/pop3/index.docbook
/usr/share/doc/HTML/fr/kioslave5/pop3/index.cache.bz2
/usr/share/doc/HTML/fr/kioslave5/pop3/index.docbook
/usr/share/doc/HTML/gl/kioslave5/pop3/index.cache.bz2
/usr/share/doc/HTML/gl/kioslave5/pop3/index.docbook
/usr/share/doc/HTML/it/kioslave5/pop3/index.cache.bz2
/usr/share/doc/HTML/it/kioslave5/pop3/index.docbook
/usr/share/doc/HTML/ko/kioslave5/pop3/index.cache.bz2
/usr/share/doc/HTML/ko/kioslave5/pop3/index.docbook
/usr/share/doc/HTML/nl/kioslave5/pop3/index.cache.bz2
/usr/share/doc/HTML/nl/kioslave5/pop3/index.docbook
/usr/share/doc/HTML/pt/kioslave5/pop3/index.cache.bz2
/usr/share/doc/HTML/pt/kioslave5/pop3/index.docbook
/usr/share/doc/HTML/pt_BR/kioslave5/pop3/index.cache.bz2
/usr/share/doc/HTML/pt_BR/kioslave5/pop3/index.docbook
/usr/share/doc/HTML/ru/kioslave5/pop3/index.cache.bz2
/usr/share/doc/HTML/ru/kioslave5/pop3/index.docbook
/usr/share/doc/HTML/sr/kioslave5/pop3/index.cache.bz2
/usr/share/doc/HTML/sr/kioslave5/pop3/index.docbook
/usr/share/doc/HTML/sr@latin/kioslave5/pop3/index.cache.bz2
/usr/share/doc/HTML/sr@latin/kioslave5/pop3/index.docbook
/usr/share/doc/HTML/sv/kioslave5/pop3/index.cache.bz2
/usr/share/doc/HTML/sv/kioslave5/pop3/index.docbook
/usr/share/doc/HTML/tr/kioslave5/pop3/index.cache.bz2
/usr/share/doc/HTML/tr/kioslave5/pop3/index.docbook
/usr/share/doc/HTML/uk/kioslave5/pop3/index.cache.bz2
/usr/share/doc/HTML/uk/kioslave5/pop3/index.docbook

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libakonadi-filestore.so.5.24.3
/V3/usr/lib64/libakonadi-singlefileresource.so.5.24.3
/V3/usr/lib64/libfolderarchivesettings.so.5.24.3
/V3/usr/lib64/libkmindexreader.so.5.24.3
/V3/usr/lib64/libmaildir.so.5.24.3
/V3/usr/lib64/qt5/plugins/kf5/kio/akonadi.so
/V3/usr/lib64/qt5/plugins/pim5/akonadi/config/akonotesconfig.so
/V3/usr/lib64/qt5/plugins/pim5/akonadi/config/birthdaysconfig.so
/V3/usr/lib64/qt5/plugins/pim5/akonadi/config/contactsconfig.so
/V3/usr/lib64/qt5/plugins/pim5/akonadi/config/googleconfig.so
/V3/usr/lib64/qt5/plugins/pim5/akonadi/config/icalconfig.so
/V3/usr/lib64/qt5/plugins/pim5/akonadi/config/icaldirconfig.so
/V3/usr/lib64/qt5/plugins/pim5/akonadi/config/maildirconfig.so
/V3/usr/lib64/qt5/plugins/pim5/akonadi/config/maildispatcherconfig.so
/V3/usr/lib64/qt5/plugins/pim5/akonadi/config/mboxconfig.so
/V3/usr/lib64/qt5/plugins/pim5/akonadi/config/mixedmaildirconfig.so
/V3/usr/lib64/qt5/plugins/pim5/akonadi/config/newmailnotifierconfig.so
/V3/usr/lib64/qt5/plugins/pim5/akonadi/config/notesconfig.so
/V3/usr/lib64/qt5/plugins/pim5/akonadi/config/openxchangeconfig.so
/V3/usr/lib64/qt5/plugins/pim5/akonadi/config/pop3config.so
/V3/usr/lib64/qt5/plugins/pim5/akonadi/config/tomboynotesconfig.so
/V3/usr/lib64/qt5/plugins/pim5/akonadi/config/vcardconfig.so
/V3/usr/lib64/qt5/plugins/pim5/akonadi/config/vcarddirconfig.so
/V3/usr/lib64/qt5/plugins/pim5/kcms/kaddressbook/kcm_ldap.so
/V3/usr/lib64/qt5/plugins/pim5/mailtransport/mailtransport_akonadiplugin.so
/usr/lib64/libakonadi-filestore.so.5
/usr/lib64/libakonadi-filestore.so.5.24.3
/usr/lib64/libakonadi-singlefileresource.so.5
/usr/lib64/libakonadi-singlefileresource.so.5.24.3
/usr/lib64/libfolderarchivesettings.so.5
/usr/lib64/libfolderarchivesettings.so.5.24.3
/usr/lib64/libkmindexreader.so.5
/usr/lib64/libkmindexreader.so.5.24.3
/usr/lib64/libmaildir.so.5
/usr/lib64/libmaildir.so.5.24.3
/usr/lib64/qt5/plugins/kf5/kio/akonadi.so
/usr/lib64/qt5/plugins/pim5/akonadi/config/akonotesconfig.so
/usr/lib64/qt5/plugins/pim5/akonadi/config/birthdaysconfig.so
/usr/lib64/qt5/plugins/pim5/akonadi/config/contactsconfig.so
/usr/lib64/qt5/plugins/pim5/akonadi/config/googleconfig.so
/usr/lib64/qt5/plugins/pim5/akonadi/config/icalconfig.so
/usr/lib64/qt5/plugins/pim5/akonadi/config/icaldirconfig.so
/usr/lib64/qt5/plugins/pim5/akonadi/config/maildirconfig.so
/usr/lib64/qt5/plugins/pim5/akonadi/config/maildispatcherconfig.so
/usr/lib64/qt5/plugins/pim5/akonadi/config/mboxconfig.so
/usr/lib64/qt5/plugins/pim5/akonadi/config/mixedmaildirconfig.so
/usr/lib64/qt5/plugins/pim5/akonadi/config/newmailnotifierconfig.so
/usr/lib64/qt5/plugins/pim5/akonadi/config/notesconfig.so
/usr/lib64/qt5/plugins/pim5/akonadi/config/openxchangeconfig.so
/usr/lib64/qt5/plugins/pim5/akonadi/config/pop3config.so
/usr/lib64/qt5/plugins/pim5/akonadi/config/tomboynotesconfig.so
/usr/lib64/qt5/plugins/pim5/akonadi/config/vcardconfig.so
/usr/lib64/qt5/plugins/pim5/akonadi/config/vcarddirconfig.so
/usr/lib64/qt5/plugins/pim5/kcms/kaddressbook/kcm_ldap.so
/usr/lib64/qt5/plugins/pim5/mailtransport/mailtransport_akonadiplugin.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kdepim-runtime/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/kdepim-runtime/2a638514c87c4923c0570c55822620fad56f2a33
/usr/share/package-licenses/kdepim-runtime/6091db0aead0d90182b93d3c0d09ba93d188f907
/usr/share/package-licenses/kdepim-runtime/680ed9349d3d12bd39ddd36e8c4bc6b1b0cb1c0e
/usr/share/package-licenses/kdepim-runtime/6f1f675aa5f6a2bbaa573b8343044b166be28399
/usr/share/package-licenses/kdepim-runtime/757b86330df80f81143d5916b3e92b4bcb1b1890
/usr/share/package-licenses/kdepim-runtime/7d9831e05094ce723947d729c2a46a09d6e90275
/usr/share/package-licenses/kdepim-runtime/8287b608d3fa40ef401339fd907ca1260c964123
/usr/share/package-licenses/kdepim-runtime/971f2a85c02441da0d59ff0790511592a0114532
/usr/share/package-licenses/kdepim-runtime/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
/usr/share/package-licenses/kdepim-runtime/e458941548e0864907e654fa2e192844ae90fc32
/usr/share/package-licenses/kdepim-runtime/e712eadfab0d2357c0f50f599ef35ee0d87534cb

%files locales -f accountwizard_contacts.lang -f accountwizard_ews.lang -f accountwizard_ical.lang -f accountwizard_imap.lang -f accountwizard_kolab.lang -f accountwizard_mailbox.lang -f accountwizard_maildir.lang -f accountwizard_pop3.lang -f accountwizard_vcard.lang -f accountwizard_vcarddir.lang -f akonadi-filestore.lang -f akonadi_birthdays_resource.lang -f akonadi_contacts_resource.lang -f akonadi_davgroupware_resource.lang -f akonadi_etesync_resource.lang -f akonadi_ews_resource.lang -f akonadi_google_resource.lang -f akonadi_ical_resource.lang -f akonadi_icaldir_resource.lang -f akonadi_imap_resource.lang -f akonadi_maildir_resource.lang -f akonadi_maildispatcher_agent.lang -f akonadi_mbox_resource.lang -f akonadi_migration_agent.lang -f akonadi_mixedmaildir_resource.lang -f akonadi_newmailnotifier_agent.lang -f akonadi_openxchange_resource.lang -f akonadi_pop3_resource.lang -f akonadi_singlefile_resource.lang -f akonadi_tomboynotes_resource.lang -f akonadi_vcard_resource.lang -f akonadi_vcarddir_resource.lang -f gid-migrator.lang -f kio_akonadi.lang -f libfolderarchivesettings.lang
%defattr(-,root,root,-)

