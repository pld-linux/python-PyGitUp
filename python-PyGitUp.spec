#
# Conditional build:
%bcond_without	python2	# CPython 2.x module
%bcond_without	python3	# CPython 3.x module
%bcond_without	tests	# unit tests

%define		module	PyGitUp
Summary:	git-up(1) - fetch and rebase all locally-tracked remote branches
Summary(pl.UTF-8):	git-up(1) - pobieranie i rebase wszystkich śledzonych lokalnie zdanych gałęzi
Name:		python-%{module}
Version:	1.6.1
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://github.com/msiemens/PyGitUp/releases
Source0:	https://github.com/msiemens/PyGitUp/archive/v%{version}/%{module}-v%{version}.tar.gz
# Source0-md5:	8573a0c48aa0afa6dddae51d1cd204c1
URL:		https://github.com/msiemens/PyGitUp
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-click >= 7.0
BuildRequires:	python-colorama >= 0.3.7
BuildRequires:	python-git >= 2.1.8
BuildRequires:	python-nose >= 1.3.7
BuildRequires:	python-six >= 1.10.0
BuildRequires:	python-termcolor >= 1.1.0
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.4
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-click >= 7.0
BuildRequires:	python3-colorama >= 0.3.7
BuildRequires:	python3-git >= 2.1.8
BuildRequires:	python3-nose >= 1.3.7
BuildRequires:	python3-six >= 1.10.0
BuildRequires:	python3-termcolor >= 1.1.0
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
git-up(1) - fetch and rebase all locally-tracked remote branches.

%description -l pl.UTF-8
git-up(1) - pobieranie i rebase wszystkich śledzonych lokalnie zdanych
gałęzi.

%package -n python3-%{module}
Summary:	git-up(1) - fetch and rebase all locally-tracked remote branches
Summary(pl.UTF-8):	git-up(1) - pobieranie i rebase wszystkich śledzonych lokalnie zdanych gałęzi
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.4

%description -n python3-%{module}
git-up(1) - fetch and rebase all locally-tracked remote branches.

%description -n python3-%{module} -l pl.UTF-8
git-up(1) - pobieranie i rebase wszystkich śledzonych lokalnie zdanych
gałęzi.

%prep
%setup -q -n %{module}-%{version}

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python3}
%py3_install

%{__mv} $RPM_BUILD_ROOT%{_bindir}/git-up{,-3}

%{__rm} -r $RPM_BUILD_ROOT%{py3_sitescriptdir}/PyGitUp/tests
%endif

%if %{with python2}
%py_install

%py_postclean

%{__rm} -r $RPM_BUILD_ROOT%{py_sitescriptdir}/PyGitUp/tests
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc LICENCE README.rst
%attr(755,root,root) %{_bindir}/git-up
%dir %{py_sitescriptdir}/PyGitUp
%{py_sitescriptdir}/PyGitUp/*.py[co]
%{py_sitescriptdir}/PyGitUp/check-bundler.rb
%{py_sitescriptdir}/git_up-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc LICENCE README.rst
%attr(755,root,root) %{_bindir}/git-up-3
%dir %{py3_sitescriptdir}/PyGitUp
%{py3_sitescriptdir}/PyGitUp/*.py
%{py3_sitescriptdir}/PyGitUp/__pycache__
%{py3_sitescriptdir}/PyGitUp/check-bundler.rb
%{py3_sitescriptdir}/git_up-%{version}-py*.egg-info
%endif
