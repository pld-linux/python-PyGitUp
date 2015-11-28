#
# Conditional build:
%bcond_with	tests	# do not perform "make test"

%define		module	PyGitUp
Summary:	git-up(1) -- fetch and rebase all locally-tracked remote branches
Name:		python-%{module}
Version:	1.1.5
Release:	2
License:	BSD
Group:		Libraries/Python
Source0:	https://github.com/msiemens/PyGitUp/archive/v%{version}.tar.gz?/%{module}-v%{version}.tar.gz
# Source0-md5:	9d271f0b1867307efbb8365ae88fe941
Patch0:		requirements.patch
URL:		https://github.com/msiemens/PyGitUp
BuildRequires:	rpm-pythonprov
# if py_postclean is used
BuildRequires:	rpmbuild(macros) >= 1.219
BuildRequires:	python-git >= 0.3.2.1
BuildRequires:	python-async
BuildRequires:	python-colorama >= 0.2.4
BuildRequires:	python-distribute
BuildRequires:	python-docopt >= 0.6.1
BuildRequires:	python-gitdb
BuildRequires:	python-nose
BuildRequires:	python-smmap
BuildRequires:	python-termcolor >= 1.1.0
Requires:	python-git >= 0.3.2-0.RC1.2
Requires:	python-async
Requires:	python-colorama >= 0.2.4
Requires:	python-docopt >= 0.6.1
Requires:	python-gitdb
Requires:	python-modules
Requires:	python-nose
Requires:	python-smmap
Requires:	python-termcolor >= 1.1.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
git-up(1) -- fetch and rebase all locally-tracked remote branches.

%prep
%setup -q -n %{module}-%{version}
%patch0 -p1

%build
%py_build %{?with_tests:test}

%install
rm -rf $RPM_BUILD_ROOT

%py_install

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.rst
%attr(755,root,root) %{_bindir}/git-up
%attr(755,root,root) %{_bindir}/gitup.py
%dir %{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{module}/*.py[co]
%{py_sitescriptdir}/%{module}/check-bundler.rb
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/git_up-*.egg-info
%endif
