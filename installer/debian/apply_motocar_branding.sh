#!/usr/bin/env bash
set -euo pipefail

# Aplica a identidade visual MotocarPABX (logos, favicon, tema branco/vermelho e remoção de anúncios)
# em uma instalação FreePBX 17 no Debian 12.

if [[ "${EUID}" -ne 0 ]]; then
  echo "Execute como root (ex.: sudo bash $0)" >&2
  exit 1
fi

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/../.." && pwd)"
FW_ADMIN="${REPO_ROOT}/freepbx/framework/amp_conf/htdocs/admin"
DASHBOARD_MOD="${REPO_ROOT}/freepbx/modules/dashboard"
WEB_ADMIN="/var/www/html/admin"

if [[ ! -d "${WEB_ADMIN}" ]]; then
  echo "Diretório ${WEB_ADMIN} não encontrado. Instale o FreePBX 17 antes de executar." >&2
  exit 1
fi

echo "==> Copiando assets visuais MotocarPABX..."
install -d "${WEB_ADMIN}/images" "${WEB_ADMIN}/assets/images" "${WEB_ADMIN}/assets/css" "${WEB_ADMIN}/assets/less/freepbx"
cp "${FW_ADMIN}/images/motocar-favicon.ico" "${WEB_ADMIN}/images/motocar-favicon.ico"
cp "${FW_ADMIN}/images/motocar-logo-nav.png" "${WEB_ADMIN}/images/motocar-logo-nav.png"
cp "${FW_ADMIN}/images/motocar-logo-footer.png" "${WEB_ADMIN}/images/motocar-logo-footer.png"
cp "${FW_ADMIN}/images/motocar-logo-login.png" "${WEB_ADMIN}/images/motocar-logo-login.png"
cp "${FW_ADMIN}/images/motocar-favicon.ico" "${WEB_ADMIN}/images/favicon.ico"
cp "${FW_ADMIN}/images/motocar-logo-nav.png" "${WEB_ADMIN}/images/tango.png"
cp "${FW_ADMIN}/images/motocar-logo-nav.png" "${WEB_ADMIN}/images/freepbx.png"
cp "${FW_ADMIN}/images/motocar-logo-footer.png" "${WEB_ADMIN}/images/freepbx_small.png"
cp "${FW_ADMIN}/assets/images/badge.png" "${WEB_ADMIN}/assets/images/badge.png"
rm -f "${WEB_ADMIN}/images/sangoma-horizontal_thumb.png" "${WEB_ADMIN}/images/schmooze-logo.png"

echo "==> Aplicando tema branco e vermelho..."
cp "${FW_ADMIN}/assets/less/freepbx/variables.less" "${WEB_ADMIN}/assets/less/freepbx/variables.less"
cp "${FW_ADMIN}/assets/less/freepbx/search.less" "${WEB_ADMIN}/assets/less/freepbx/search.less"
cp "${FW_ADMIN}/assets/css/motocar-theme.css" "${WEB_ADMIN}/assets/css/motocar-theme.css"
cp "${FW_ADMIN}/assets/js/script.legacy.js" "${WEB_ADMIN}/assets/js/script.legacy.js"

echo "==> Aplicando views e limpeza de anúncios..."
cp "${FW_ADMIN}/config.php" "${WEB_ADMIN}/config.php"
cp "${FW_ADMIN}/libraries/BMO/OOBE.class.php" "${WEB_ADMIN}/libraries/BMO/OOBE.class.php"
cp "${FW_ADMIN}/views/header.php" "${WEB_ADMIN}/views/header.php"
cp "${FW_ADMIN}/views/footer.php" "${WEB_ADMIN}/views/footer.php"
cp "${FW_ADMIN}/views/footer_content.php" "${WEB_ADMIN}/views/footer_content.php"
cp "${FW_ADMIN}/views/login.php" "${WEB_ADMIN}/views/login.php"
cp "${FW_ADMIN}/views/menu.php" "${WEB_ADMIN}/views/menu.php"
cp "${FW_ADMIN}/views/menu_items.php" "${WEB_ADMIN}/views/menu_items.php"
cp "${FW_ADMIN}/views/welcome.php" "${WEB_ADMIN}/views/welcome.php"
cp "${FW_ADMIN}/views/module_admin/tab-modules.php" "${WEB_ADMIN}/views/module_admin/tab-modules.php"
cp "${FW_ADMIN}/views/module_admin/reposelect.php" "${WEB_ADMIN}/views/module_admin/reposelect.php"

if [[ -f "${WEB_ADMIN}/modules/core/module.xml" ]]; then
  sed -i '/FreePBX Support/d' "${WEB_ADMIN}/modules/core/module.xml"
fi

if [[ -d "${WEB_ADMIN}/modules/dashboard/sections" ]]; then
  cp "${DASHBOARD_MOD}/sections/Blogs.class.php" "${WEB_ADMIN}/modules/dashboard/sections/Blogs.class.php"
fi

UCP_MOD="${REPO_ROOT}/freepbx/modules/ucp"
if [[ -d "${WEB_ADMIN}/modules/ucp/htdocs/views" ]]; then
  cp "${UCP_MOD}/htdocs/views/dashfootercontent.php" "${WEB_ADMIN}/modules/ucp/htdocs/views/dashfootercontent.php"
  cp "${UCP_MOD}/htdocs/views/dashboard-header.php" "${WEB_ADMIN}/modules/ucp/htdocs/views/dashboard-header.php"
  install -d "${WEB_ADMIN}/modules/ucp/htdocs/images"
  cp "${FW_ADMIN}/images/motocar-logo-nav.png" "${WEB_ADMIN}/modules/ucp/htdocs/images/motocar-logo-nav.png"
  cp "${FW_ADMIN}/images/motocar-logo-footer.png" "${WEB_ADMIN}/modules/ucp/htdocs/images/motocar-logo-footer.png"
  cp "${FW_ADMIN}/images/motocar-favicon.ico" "${WEB_ADMIN}/modules/ucp/htdocs/images/motocar-favicon.ico"
  rm -f "${WEB_ADMIN}/modules/ucp/htdocs/images/sangoma-horizontal_thumb.png"
fi

echo "==> Aplicando traduções completas em Português (pt_BR)..."
install -d "${WEB_ADMIN}/i18n/pt_BR/LC_MESSAGES"
cp "${FW_ADMIN}/i18n/pt_BR/LC_MESSAGES/amp.po" "${WEB_ADMIN}/i18n/pt_BR/LC_MESSAGES/amp.po"
cp "${FW_ADMIN}/i18n/pt_BR/LC_MESSAGES/amp.mo" "${WEB_ADMIN}/i18n/pt_BR/LC_MESSAGES/amp.mo"
if [[ -d "${WEB_ADMIN}/modules/dashboard/i18n/pt_BR/LC_MESSAGES" ]]; then
  cp "${DASHBOARD_MOD}/i18n/pt_BR/LC_MESSAGES/dashboard.po" "${WEB_ADMIN}/modules/dashboard/i18n/pt_BR/LC_MESSAGES/dashboard.po"
  cp "${DASHBOARD_MOD}/i18n/pt_BR/LC_MESSAGES/dashboard.mo" "${WEB_ADMIN}/modules/dashboard/i18n/pt_BR/LC_MESSAGES/dashboard.mo"
fi

echo "==> Garantindo locale pt_BR.UTF-8 no sistema..."
if ! locale -a | grep -qiE '^pt_BR\.utf-?8$'; then
  if [[ -f /etc/locale.gen ]]; then
    sed -i 's/^# *pt_BR\.UTF-8 UTF-8/pt_BR.UTF-8 UTF-8/' /etc/locale.gen
    if ! grep -q '^pt_BR\.UTF-8 UTF-8' /etc/locale.gen; then
      echo 'pt_BR.UTF-8 UTF-8' >> /etc/locale.gen
    fi
  fi
  locale-gen pt_BR.UTF-8 || locale-gen
fi

echo "==> Removendo módulos comerciais e propagandas..."
for mod in firewall sysadmin cos cdrpro oracle_connector pms restapps; do
  fwconsole ma -f delete "${mod}" >/dev/null 2>&1 || true
done
while IFS= read -r cmod; do
  [[ -n "${cmod}" ]] && fwconsole ma -f delete "${cmod}" >/dev/null 2>&1 || true
done < <(fwconsole ma list 2>/dev/null | awk -F'|' '/Commercial/ {gsub(/ /, "", $2); if ($2 != "") print $2}')
fwconsole ma disablerepo commercial >/dev/null 2>&1 || true
fwconsole ma enablerepo standard >/dev/null 2>&1 || true

echo "==> Atualizando configurações no FreePBX (fwconsole)..."
fwconsole setting BRAND_TITLE "MotocarPABX"
fwconsole setting DASHBOARD_FREEPBX_BRAND "MotocarPABX"
fwconsole setting BRAND_IMAGE_FAVICON "images/motocar-favicon.ico"
fwconsole setting BRAND_IMAGE_TANGO_LEFT "images/motocar-logo-nav.png"
fwconsole setting BRAND_IMAGE_FREEPBX_FOOT "images/motocar-logo-footer.png"
fwconsole setting BRAND_FREEPBX_ALT_LEFT "MotocarPABX"
fwconsole setting BRAND_FREEPBX_ALT_FOOT "MotocarPABX"
fwconsole setting BRAND_SPONSOR_ALT_FOOT ""
fwconsole setting BRAND_IMAGE_SPONSOR_FOOT ""
fwconsole setting BRAND_IMAGE_FREEPBX_LINK_LEFT "config.php"
fwconsole setting BRAND_IMAGE_FREEPBX_LINK_FOOT "config.php"
fwconsole setting BRAND_IMAGE_SPONSOR_LINK_FOOT ""
fwconsole setting BRAND_CSS_CUSTOM "assets/css/motocar-theme.css"
fwconsole setting RSSFEEDS ""
fwconsole setting UCPRSSFEEDS "" >/dev/null 2>&1 || true
fwconsole setting BROWSER_STATS 0
fwconsole setting SIGNATURECHECK 0
fwconsole setting UIDEFAULTLANG "pt_BR"
fwconsole setting FREEPBX_SYSTEM_IDENT "MotocarPABX"
php -r 'include "/etc/freepbx.conf"; $nt = \notifications::create($db); $nt->delete("freepbx", "SIGNATURE_TAMPERED"); $nt->delete("freepbx", "SIGNATURE_UNSIGNED");' >/dev/null 2>&1 || true

echo "==> Limpando cache LESS/JS e ajustando permissões..."
rm -rf "${WEB_ADMIN}/assets/less/cache/"* "${WEB_ADMIN}/assets/js/pbxlib_"*.js
chown -R asterisk:asterisk "${WEB_ADMIN}"

echo "==> Reiniciando Apache..."
systemctl restart apache2

echo "MotocarPABX: identidade visual aplicada com sucesso!"
