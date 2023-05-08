#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-HTML-TreeBuilder
Version  : 5.07
Release  : 12
URL      : https://cpan.metacpan.org/authors/id/K/KE/KENTNL/HTML-Tree-5.07.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/K/KE/KENTNL/HTML-Tree-5.07.tar.gz
Summary  : 'Work with HTML in a DOM-like tree structure'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-HTML-TreeBuilder-bin = %{version}-%{release}
Requires: perl-HTML-TreeBuilder-license = %{version}-%{release}
Requires: perl-HTML-TreeBuilder-man = %{version}-%{release}
Requires: perl-HTML-TreeBuilder-perl = %{version}-%{release}
Requires: perl(HTML::Entities)
Requires: perl(HTML::Parser)
Requires: perl(HTML::Tagset)
BuildRequires : buildreq-cpan
BuildRequires : perl(HTML::Entities)
BuildRequires : perl(HTML::Parser)
BuildRequires : perl(HTML::Tagset)
BuildRequires : perl(Test::Fatal)

%description
HTML-Tree version 5.07, released 2017-08-31
This distribution contains a suite of modules for representing,
creating, and extracting information from HTML syntax trees; there is
also relevent documentation.  These modules used to be part of the
libwww-perl distribution, but are now unbundled in order to facilitate
a separate development track.  Bug reports and discussions about these
modules can be sent to the RT queue at <bug-html-tree@rt.cpan.org>.

%package bin
Summary: bin components for the perl-HTML-TreeBuilder package.
Group: Binaries
Requires: perl-HTML-TreeBuilder-license = %{version}-%{release}

%description bin
bin components for the perl-HTML-TreeBuilder package.


%package dev
Summary: dev components for the perl-HTML-TreeBuilder package.
Group: Development
Requires: perl-HTML-TreeBuilder-bin = %{version}-%{release}
Provides: perl-HTML-TreeBuilder-devel = %{version}-%{release}
Requires: perl-HTML-TreeBuilder = %{version}-%{release}

%description dev
dev components for the perl-HTML-TreeBuilder package.


%package license
Summary: license components for the perl-HTML-TreeBuilder package.
Group: Default

%description license
license components for the perl-HTML-TreeBuilder package.


%package man
Summary: man components for the perl-HTML-TreeBuilder package.
Group: Default

%description man
man components for the perl-HTML-TreeBuilder package.


%package perl
Summary: perl components for the perl-HTML-TreeBuilder package.
Group: Default
Requires: perl-HTML-TreeBuilder = %{version}-%{release}

%description perl
perl components for the perl-HTML-TreeBuilder package.


%prep
%setup -q -n HTML-Tree-5.07
cd %{_builddir}/HTML-Tree-5.07

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-HTML-TreeBuilder
cp %{_builddir}/HTML-Tree-5.07/LICENSE %{buildroot}/usr/share/package-licenses/perl-HTML-TreeBuilder/309a589f389ca0257473439676541372e4128bc8
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/htmltree

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/HTML::AsSubs.3
/usr/share/man/man3/HTML::Element.3
/usr/share/man/man3/HTML::Element::traverse.3
/usr/share/man/man3/HTML::Parse.3
/usr/share/man/man3/HTML::Tree.3
/usr/share/man/man3/HTML::Tree::AboutObjects.3
/usr/share/man/man3/HTML::Tree::AboutTrees.3
/usr/share/man/man3/HTML::Tree::Scanning.3
/usr/share/man/man3/HTML::TreeBuilder.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-HTML-TreeBuilder/309a589f389ca0257473439676541372e4128bc8

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/htmltree.1

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
