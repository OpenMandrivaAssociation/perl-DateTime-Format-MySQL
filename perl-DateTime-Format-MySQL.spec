%define upstream_name    DateTime-Format-MySQL
%define upstream_version 0.04

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    6

Summary:    Parse and format MySQL dates and times
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/DateTime/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Class::Factory::Util)
BuildRequires: perl(DateTime)
BuildRequires: perl(DateTime::Format::Builder)
BuildRequires: perl(Module::Build::Compat)

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

Requires: perl(Class::Factory::Util)
Requires: perl(DateTime::Format::Builder)

%description
This module understands the formats used by MySQL for its DATE, DATETIME,
TIME, and TIMESTAMP data types. It can be used to parse these formats in
order to create DateTime objects, and it can take a DateTime object and
produce a string representing it in the MySQL format.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes LICENSE README
%{_mandir}/man3/*
%perl_vendorlib/*


%changelog
* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 0.40.0-4mdv2011.0
+ Revision: 654912
- rebuild for updated spec-helper

* Sun Nov 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.40.0-3mdv2011.0
+ Revision: 471498
- adding missing requires:

* Sun Nov 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.40.0-2mdv2010.1
+ Revision: 471458
- bump mkrel
- adding missing requires:

* Sun Nov 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.40.0-1mdv2010.1
+ Revision: 471398
- adding missing buildrequires:
- import perl-DateTime-Format-MySQL


* Sun Nov 29 2009 cpan2dist 0.04-1mdv
- initial mdv release, generated with cpan2dist
