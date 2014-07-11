%define _enable_debug_packages %{nil}
%define debug_package          %{nil}

%define src_ver 0.50-0
%define languageenglazy Walloon
%define languagecode wa
%define lc_ctype wa_BE

Summary:	%{languageenglazy} files for aspell
Summary(wa):	Coridjrece aspell e walon
Name:		aspell-%{languagecode}
Version:	0.50.0
Release:	18
Group:		System/Internationalization
License:	GPLv2
Url:		http://aspell.net/
Source0:	http://ftp.gnu.org/gnu/aspell/dict/%{languagecode}/aspell-%{languagecode}-%{src_ver}.tar.bz2

BuildRequires:	aspell >= 0.50
Requires:	aspell >= 0.50
# Mandriva Stuff
Requires:	locales-%{languagecode}
# aspell = 1, myspell = 2, lang-specific = 3
Provides:	enchant-dictionary = 1
Provides:	aspell-dictionary
Provides:	aspell-%{lc_ctype}
Provides:	spell-%{languagecode}
Autoreqprov:	no

%description
A %{languageenglazy} dictionary for use with aspell, a spelling checker.

%description
Li motî walon pol coridjrece aspell.
Avou ci chal vos ploz croidjî tos vos tecses sicrîts e rfondou walon.

%prep
%setup -qn %{name}-%{src_ver}

%build
# don't use configure macro
./configure

%make

%install
%makeinstall_std

mv README README.%{languagecode}
chmod 644 Copyright README* doc/*

%files
%doc README* Copyright doc/*
%{_libdir}/aspell-*/*

