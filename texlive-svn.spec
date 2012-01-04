# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/svn
# catalog-date 2009-03-04 19:42:30 +0100
# catalog-license lppl1.3
# catalog-version 43
Name:		texlive-svn
Version:	43
Release:	2
Summary:	Typeset Subversion keywords
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/svn
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/svn.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/svn.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/svn.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The svn package lets you typeset (in LaTeX) the value of
Subversion keywords. It is approximately an equivalent to the
rcs package, but for Subversion rather than CVS. Details of
Subversion (a replacement for CVS) is available from the
project's home site.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/svn/svn.sty
%doc %{_texmfdistdir}/doc/latex/svn/README
%doc %{_texmfdistdir}/doc/latex/svn/svn.pdf
#- source
%doc %{_texmfdistdir}/source/latex/svn/Makefile
%doc %{_texmfdistdir}/source/latex/svn/svn.dtx
%doc %{_texmfdistdir}/source/latex/svn/svn.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
