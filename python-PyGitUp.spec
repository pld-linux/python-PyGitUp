#
# Conditional build:
%bcond_with	tests	# do not perform "make test"

%define		module	PyGitUp
Summary:	git-up(1) -- fetch and rebase all locally-tracked remote branches
Name:		python-%{module}
Version:	1.4.6
Release:	1
License:	BSD
Group:		Libraries/Python
Source0:	https://github.com/msiemens/PyGitUp/archive/v%{version}.tar.gz?/%{module}-v%{version}.tar.gz
# Source0-md5:	0ee651ee4625e0089284735c99cbf558
URL:		https://github.com/msiemens/PyGitUp
BuildRequires:	rpm-pythonprov
# if py_postclean is used
BuildRequires:	rpmbuild(macros) >= 1.710
BuildRequires:	python-git >= 2.1.8
BuildRequires:	python-async
BuildRequires:	python-colorama >= 0.3.7
BuildRequires:	python-click >= 6.0.0
BuildRequires:	python-distribute
BuildRequires:	python-gitdb
BuildRequires:	python-nose
BuildRequires:	python-six >= 1.10.0
BuildRequires:	python-smmap
BuildRequires:	python-termcolor >= 1.1.0
Requires:	python-git >= 2.1.8
Requires:	python-async
Requires:	python-colorama >= 0.3.7
Requires:	python-click >= 6.0.0
Requires:	python-gitdb
Requires:	python-modules
Requires:	python-nose
Requires:	python-smmap
Requires:	python-six >= 1.10.0
Requires:	python-termcolor >= 1.1.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
git-up(1) -- fetch and rebase all locally-tracked remote branches.

%prep
%setup -q -n %{module}-%{version}

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
%dir %{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{module}/*.py[co]
%dir %{py_sitescriptdir}/%{module}/tests
%{py_sitescriptdir}/%{module}/tests/*.py[co]
%{py_sitescriptdir}/%{module}/check-bundler.rb
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/git_up-*.egg-info
%endif
