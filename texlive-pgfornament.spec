Name:		texlive-pgfornament
Version:	72029
Release:	1
Summary:	Drawing of Vectorian ornaments with PGF/TikZ
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/pgfornament
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pgfornament.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pgfornament.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package allows the drawing of Vectorian ornaments (196)
with PGF/TikZ. The documentation presents the syntax and
parameters of the macro "pgfornament".

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/pgfornament
%{_texmfdistdir}/tex/generic/pgfornament
%doc %{_texmfdistdir}/doc/latex/pgfornament

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
