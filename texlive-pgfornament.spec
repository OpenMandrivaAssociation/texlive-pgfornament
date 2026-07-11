%global tl_name pgfornament
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.3
Release:	%{tl_revision}.1
Summary:	Drawing of Vectorian ornaments with PGF/TikZ
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/tkz/pgfornament
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pgfornament.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pgfornament.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package allows the drawing of Vectorian ornaments (196) with
PGF/TikZ. The documentation presents the syntax and parameters of the
macro "pgfornament".

