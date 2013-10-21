#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	XML
%define		pnam	TreeBuilder
%include	/usr/lib/rpm/macros.perl
Summary:	XML::TreeBuilder - Parser that builds a tree of XML::Element objects
Summary(pl.UTF-8):	XML::TreeBuilder - analizator tworzący drzewo obiektów XML::Element
Name:		perl-XML-TreeBuilder
Version:	5.0
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/XML/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	5549d05bb87b862c31b64d9d21ef34a0
URL:		http://search.cpan.org/dist/XML-TreeBuilder/
BuildRequires:	perl-Module-Build
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Devel-Cover
BuildRequires:	perl-HTML-Tagset >= 3.02
BuildRequires:	perl-HTML-Tree >= 4.1
BuildRequires:	perl-Test-Exception
BuildRequires:	perl-Test-Perl-Critic
BuildRequires:	perl-Test-Pod-Coverage
BuildRequires:	perl-Test-Simple
BuildRequires:	perl-XML-Catalog >= 1.0.0
BuildRequires:	perl-XML-Parser
%endif
Requires:	perl-HTML-Tagset >= 3.02
Requires:	perl-HTML-Tree >= 4.1
Requires:	perl-XML-Catalog >= 1.0.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module uses XML::Parser to make XML document trees constructed of
XML::Element objects (and XML::Element is a subclass of HTML::Element
adapted for XML). XML::TreeBuilder is meant particularly for people
who are used to the HTML::TreeBuilder / HTML::Element interface to
document trees, and who don't want to learn some other document
interface like XML::Twig or XML::DOM.

%description -l pl.UTF-8
Ten moduł wykorzystuje XML::Parser do tworzenia drzew dokumentów XML
skonstruowanych z obiektów XML::Element (XML::Element jest podklasą
HTML::Element zaadaptowaną dla XML-a). XML::TreeBuilder jest
przeznaczony w szczególności dla korzystających z interfejsu
HTML::TreeBuilder / HTML::Element do drzew dokumentów, nie chcących
uczyć się innych interfejsów do dokumentów, takich jak XML::Twig czy
XML::DOM.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/XML/Element.pm
%{perl_vendorlib}/XML/TreeBuilder.pm
%{_mandir}/man3/XML::Element.3pm*
%{_mandir}/man3/XML::TreeBuilder.3pm*
