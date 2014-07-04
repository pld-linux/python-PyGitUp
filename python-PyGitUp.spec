#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		module	PyGitUp
Summary:	git-up(1) -- fetch and rebase all locally-tracked remote branches
Name:		python-%{module}
Version:	1.1.4
Release:	0.1
License:	BSD
Group:		Libraries/Python
Source0:	https://github.com/msiemens/PyGitUp/archive/v%{version}.tar.gz?/%{module}-v%{version}.tar.gz
# Source0-md5:	fd7d89489bb045853077909fe0fd95aa
URL:		https://github.com/msiemens/PyGitUp
BuildRequires:	rpm-pythonprov
# if py_postclean is used
BuildRequires:	rpmbuild(macros) >= 1.219
BuildRequires:	python-git >= 0.3.2-0.RC1.2
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

%build
%{__python} setup.py build %{?with_tests:test}

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py \
	install --skip-build \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS CREDITS ChangeLog NEWS README THANKS TODO
%{py_sitescriptdir}/*.py[co]
%attr(755,root,root) %{py_sitescriptdir}/*.so
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/TEMPLATE-*.egg-info
%endif
