#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : kdepim-runtime
Version  : 19.08.3
Release  : 4
URL      : https://download.kde.org/stable/applications/19.08.3/src/kdepim-runtime-19.08.3.tar.xz
Source0  : https://download.kde.org/stable/applications/19.08.3/src/kdepim-runtime-19.08.3.tar.xz
Source1 : https://download.kde.org/stable/applications/19.08.3/src/kdepim-runtime-19.08.3.tar.xz.sig
Summary  : Extends the functionality of kdepim
Group    : Development/Tools
License  : AGPL-3.0 BSD-2-Clause GPL-2.0 GPL-3.0 LGPL-2.1 LGPL-3.0
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
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules pkgconfig(libsasl2)
BuildRequires : extra-cmake-modules shared-mime-info
BuildRequires : kalarmcal-dev
BuildRequires : kcalcore-dev
BuildRequires : kcalutils-dev
BuildRequires : kcontacts-dev
BuildRequires : kdav-dev
BuildRequires : kholidays-dev
BuildRequires : kidentitymanagement-dev
BuildRequires : kmailtransport-dev
BuildRequires : kmbox-dev
BuildRequires : kmime-dev
BuildRequires : knotifyconfig-dev
BuildRequires : kpimtextedit-dev
BuildRequires : libkgapi-dev
BuildRequires : pimcommon-dev
BuildRequires : qca-qt5-dev
BuildRequires : qtbase-dev mesa-dev
BuildRequires : qtwebengine-dev

%description
==== What's this ? ====
This is an Akonadi resource to access DAV-enabled PIM storages.

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
%setup -q -n kdepim-runtime-19.08.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1573530958
mkdir -p clr-build
pushd clr-build
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}  VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1573530958
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kdepim-runtime
cp %{_builddir}/kdepim-runtime-19.08.3/COPYING %{buildroot}/usr/share/package-licenses/kdepim-runtime/7c203dee3a03037da436df03c4b25b659c073976
cp %{_builddir}/kdepim-runtime-19.08.3/COPYING.LIB %{buildroot}/usr/share/package-licenses/kdepim-runtime/9a1929f4700d2407c70b507b3b2aaf6226a9543c
cp %{_builddir}/kdepim-runtime-19.08.3/COPYING.agpl3 %{buildroot}/usr/share/package-licenses/kdepim-runtime/4c665f87b5dc2e7d26279c4b48968d085e1ace32
cp %{_builddir}/kdepim-runtime-19.08.3/COPYING.gpl3 %{buildroot}/usr/share/package-licenses/kdepim-runtime/31a3d460bb3c7d98845187c716a30db81c44b615
cp %{_builddir}/kdepim-runtime-19.08.3/resources/kolab/pimkolab/COPYING %{buildroot}/usr/share/package-licenses/kdepim-runtime/8ccafa97d7e7373343b2ce9fd14325720002fd6d
cp %{_builddir}/kdepim-runtime-19.08.3/resources/kolab/pimkolab/COPYING.LIB %{buildroot}/usr/share/package-licenses/kdepim-runtime/e6ce17111fff24ac88c21978b098b9fffcdee421
cp %{_builddir}/kdepim-runtime-19.08.3/resources/kolab/pimkolab/COPYING.lgplv3 %{buildroot}/usr/share/package-licenses/kdepim-runtime/f45ee1c765646813b442ca58de72e20a64a7ddba
cp %{_builddir}/kdepim-runtime-19.08.3/resources/tomboynotes/o2/LICENSE %{buildroot}/usr/share/package-licenses/kdepim-runtime/d1199253fd73ffa134ea99cd70609a908c3bc5b9
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
%find_lang akonadi_ews_resource
%find_lang akonadi_facebook_resource
%find_lang akonadi_googlecalendar_resource
%find_lang akonadi_googlecontacts_resource
%find_lang akonadi_ical_resource
%find_lang akonadi_icaldir_resource
%find_lang akonadi_imap_resource
%find_lang akonadi_kalarm_resource
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
%find_lang kio_pop3
%find_lang libfolderarchivesettings

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/akonadi_akonotes_resource
/usr/bin/akonadi_birthdays_resource
/usr/bin/akonadi_contacts_resource
/usr/bin/akonadi_davgroupware_resource
/usr/bin/akonadi_ews_resource
/usr/bin/akonadi_ewsmta_resource
/usr/bin/akonadi_facebook_resource
/usr/bin/akonadi_googlecalendar_resource
/usr/bin/akonadi_googlecontacts_resource
/usr/bin/akonadi_ical_resource
/usr/bin/akonadi_icaldir_resource
/usr/bin/akonadi_imap_resource
/usr/bin/akonadi_kalarm_dir_resource
/usr/bin/akonadi_kalarm_resource
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
/usr/share/akonadi/agents/facebookresource.desktop
/usr/share/akonadi/agents/googlecalendarresource.desktop
/usr/share/akonadi/agents/googlecontactsresource.desktop
/usr/share/akonadi/agents/icaldirresource.desktop
/usr/share/akonadi/agents/icalresource.desktop
/usr/share/akonadi/agents/imapresource.desktop
/usr/share/akonadi/agents/kalarmdirresource.desktop
/usr/share/akonadi/agents/kalarmresource.desktop
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
/usr/share/knotifications5/akonadi_maildispatcher_agent.notifyrc
/usr/share/knotifications5/akonadi_newmailnotifier_agent.notifyrc
/usr/share/knotifications5/akonadi_pop3_resource.notifyrc
/usr/share/kservices5/akonadi.protocol
/usr/share/kservices5/akonadi/davgroupware-providers/citadel.desktop
/usr/share/kservices5/akonadi/davgroupware-providers/davical.desktop
/usr/share/kservices5/akonadi/davgroupware-providers/egroupware.desktop
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
/usr/share/kservices5/pop3.protocol
/usr/share/kservices5/pop3s.protocol
/usr/share/kservicetypes5/davgroupwareprovider.desktop
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
/usr/share/doc/HTML/it/kioslave5/pop3/index.cache.bz2
/usr/share/doc/HTML/it/kioslave5/pop3/index.docbook
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
/usr/share/doc/HTML/sv/kioslave5/pop3/index.cache.bz2
/usr/share/doc/HTML/sv/kioslave5/pop3/index.docbook
/usr/share/doc/HTML/uk/kioslave5/pop3/index.cache.bz2
/usr/share/doc/HTML/uk/kioslave5/pop3/index.docbook

%files lib
%defattr(-,root,root,-)
/usr/lib64/libakonadi-filestore.so.5
/usr/lib64/libakonadi-filestore.so.5.12.3
/usr/lib64/libakonadi-singlefileresource.so.5
/usr/lib64/libakonadi-singlefileresource.so.5.12.3
/usr/lib64/libfolderarchivesettings.so.5
/usr/lib64/libfolderarchivesettings.so.5.12.3
/usr/lib64/libkmindexreader.so.5
/usr/lib64/libkmindexreader.so.5.12.3
/usr/lib64/libmaildir.so.5
/usr/lib64/libmaildir.so.5.12.3
/usr/lib64/qt5/plugins/akonadi/config/akonotesconfig.so
/usr/lib64/qt5/plugins/akonadi/config/birthdaysconfig.so
/usr/lib64/qt5/plugins/akonadi/config/contactsconfig.so
/usr/lib64/qt5/plugins/akonadi/config/facebookconfig.so
/usr/lib64/qt5/plugins/akonadi/config/icalconfig.so
/usr/lib64/qt5/plugins/akonadi/config/icaldirconfig.so
/usr/lib64/qt5/plugins/akonadi/config/kalarmconfig.so
/usr/lib64/qt5/plugins/akonadi/config/maildirconfig.so
/usr/lib64/qt5/plugins/akonadi/config/maildispatcherconfig.so
/usr/lib64/qt5/plugins/akonadi/config/mboxconfig.so
/usr/lib64/qt5/plugins/akonadi/config/mixedmaildirconfig.so
/usr/lib64/qt5/plugins/akonadi/config/newmailnotifierconfig.so
/usr/lib64/qt5/plugins/akonadi/config/notesconfig.so
/usr/lib64/qt5/plugins/akonadi/config/openxchangeconfig.so
/usr/lib64/qt5/plugins/akonadi/config/pop3config.so
/usr/lib64/qt5/plugins/akonadi/config/tomboynotesconfig.so
/usr/lib64/qt5/plugins/akonadi/config/vcardconfig.so
/usr/lib64/qt5/plugins/akonadi/config/vcarddirconfig.so
/usr/lib64/qt5/plugins/kf5/kio/akonadi.so
/usr/lib64/qt5/plugins/kf5/kio/pop3.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kdepim-runtime/31a3d460bb3c7d98845187c716a30db81c44b615
/usr/share/package-licenses/kdepim-runtime/4c665f87b5dc2e7d26279c4b48968d085e1ace32
/usr/share/package-licenses/kdepim-runtime/7c203dee3a03037da436df03c4b25b659c073976
/usr/share/package-licenses/kdepim-runtime/8ccafa97d7e7373343b2ce9fd14325720002fd6d
/usr/share/package-licenses/kdepim-runtime/9a1929f4700d2407c70b507b3b2aaf6226a9543c
/usr/share/package-licenses/kdepim-runtime/d1199253fd73ffa134ea99cd70609a908c3bc5b9
/usr/share/package-licenses/kdepim-runtime/e6ce17111fff24ac88c21978b098b9fffcdee421
/usr/share/package-licenses/kdepim-runtime/f45ee1c765646813b442ca58de72e20a64a7ddba

%files locales -f accountwizard_contacts.lang -f accountwizard_ews.lang -f accountwizard_ical.lang -f accountwizard_imap.lang -f accountwizard_kolab.lang -f accountwizard_mailbox.lang -f accountwizard_maildir.lang -f accountwizard_pop3.lang -f accountwizard_vcard.lang -f accountwizard_vcarddir.lang -f akonadi-filestore.lang -f akonadi_birthdays_resource.lang -f akonadi_contacts_resource.lang -f akonadi_davgroupware_resource.lang -f akonadi_ews_resource.lang -f akonadi_facebook_resource.lang -f akonadi_googlecalendar_resource.lang -f akonadi_googlecontacts_resource.lang -f akonadi_ical_resource.lang -f akonadi_icaldir_resource.lang -f akonadi_imap_resource.lang -f akonadi_kalarm_resource.lang -f akonadi_maildir_resource.lang -f akonadi_maildispatcher_agent.lang -f akonadi_mbox_resource.lang -f akonadi_migration_agent.lang -f akonadi_mixedmaildir_resource.lang -f akonadi_newmailnotifier_agent.lang -f akonadi_openxchange_resource.lang -f akonadi_pop3_resource.lang -f akonadi_singlefile_resource.lang -f akonadi_tomboynotes_resource.lang -f akonadi_vcard_resource.lang -f akonadi_vcarddir_resource.lang -f gid-migrator.lang -f kio_akonadi.lang -f kio_pop3.lang -f libfolderarchivesettings.lang
%defattr(-,root,root,-)

