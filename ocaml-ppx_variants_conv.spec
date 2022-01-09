#
# Conditional build:
%bcond_without	ocaml_opt	# native optimized binaries (bytecode is always built)

# not yet available on x32 (ocaml 4.02.1), update when upstream will support it
%ifnarch %{ix86} %{x8664} %{arm} aarch64 ppc sparc sparcv9
%undefine	with_ocaml_opt
%endif

Summary:	Generation of accessor and iteration functions for OCaml variant types
Summary(pl.UTF-8):	Generowanie funkcji dostępowych i iterujących dla typów wariantowych w OCamlu
Name:		ocaml-ppx_variants_conv
Version:	0.14.2
Release:	1
License:	MIT
Group:		Libraries
#Source0Download: https://github.com/janestreet/ppx_variants_conv/tags
Source0:	https://github.com/janestreet/ppx_variants_conv/archive/v%{version}/ppx_variants_conv-%{version}.tar.gz
# Source0-md5:	de29f93732da2fad0b221edbd763f5c1
URL:		https://github.com/janestreet/ppx_variants_conv
BuildRequires:	ocaml >= 1:4.04.2
BuildRequires:	ocaml-base-devel >= 0.14
BuildRequires:	ocaml-base-devel < 0.15
BuildRequires:	ocaml-dune >= 2.0.0
BuildRequires:	ocaml-ppxlib-devel >= 0.23.0
BuildRequires:	ocaml-variantslib-devel >= 0.14
BuildRequires:	ocaml-variantslib-devel < 0.15
%requires_eq	ocaml-runtime
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		debug_package	%{nil}

%description
ppx_variants_conv is a ppx rewriter that can be used to define first
class values representing variant constructors, and additional
routines to fold, iterate and map over all constructors of a variant
type.

This package contains files needed to run bytecode executables using
ppx_variants_conv library.

%description -l pl.UTF-8
ppx_variants_conv to moduł przepisujący ppx, który można wykorzystać
do definiowania pierwszoklasowych wartości reprezentujących
konstruktory wariantowe oraz dodatkowych funkcji do zawijania,
iterowania i mapowania po wszystkich konstruktorach typów
wariantowych.

Pakiet ten zawiera binaria potrzebne do uruchamiania programów
używających biblioteki ppx_variants_conv.

%package devel
Summary:	Generation of accessor and iteration functions for OCaml variant types - development part
Summary(pl.UTF-8):	Generowanie funkcji dostępowych i iterujących dla typów wariantowych w OCamlu - część programistyczna
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
%requires_eq	ocaml
Requires:	ocaml-base-devel >= 0.14
Requires:	ocaml-ppxlib-devel >= 0.23.0
Requires:	ocaml-variantslib-devel >= 0.14

%description devel
This package contains files needed to develop OCaml programs using
ppx_variants_conv library.

%description devel -l pl.UTF-8
Pakiet ten zawiera pliki niezbędne do tworzenia programów w OCamlu
używających biblioteki ppx_variants_conv.

%prep
%setup -q -n ppx_variants_conv-%{version}

%build
dune build --verbose

%install
rm -rf $RPM_BUILD_ROOT

dune install --destdir=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -pr example/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

# sources
%{__rm} $RPM_BUILD_ROOT%{_libdir}/ocaml/ppx_variants_conv/*.ml
# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_prefix}/doc/ppx_variants_conv

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.md LICENSE.md README.md
%dir %{_libdir}/ocaml/ppx_variants_conv
%{_libdir}/ocaml/ppx_variants_conv/META
%{_libdir}/ocaml/ppx_variants_conv/*.cma
%if %{with ocaml_opt}
%attr(755,root,root) %{_libdir}/ocaml/ppx_variants_conv/*.cmxs
%endif

%files devel
%defattr(644,root,root,755)
%{_libdir}/ocaml/ppx_variants_conv/*.cmi
%{_libdir}/ocaml/ppx_variants_conv/*.cmt
%{_libdir}/ocaml/ppx_variants_conv/*.cmti
%{_libdir}/ocaml/ppx_variants_conv/*.mli
%if %{with ocaml_opt}
%{_libdir}/ocaml/ppx_variants_conv/ppx_variants_conv.a
%{_libdir}/ocaml/ppx_variants_conv/*.cmx
%{_libdir}/ocaml/ppx_variants_conv/*.cmxa
%endif
%{_libdir}/ocaml/ppx_variants_conv/dune-package
%{_libdir}/ocaml/ppx_variants_conv/opam
%{_examplesdir}/%{name}-%{version}
