#!/usr/bin/env python3
"""Atualiza traduções pt_BR (amp.po e dashboard.po) e compila os binários .mo GNU gettext."""

from pathlib import Path
import ast
import re
import struct

REPO_ROOT = Path(__file__).resolve().parents[2]
AMP_PO = REPO_ROOT / "freepbx/framework/amp_conf/htdocs/admin/i18n/pt_BR/LC_MESSAGES/amp.po"
AMP_MO = AMP_PO.with_suffix(".mo")
DASH_PO = REPO_ROOT / "freepbx/modules/dashboard/i18n/pt_BR/LC_MESSAGES/dashboard.po"
DASH_MO = DASH_PO.with_suffix(".mo")

AMP_TRANSLATIONS = {
    "%s 17 is supported only on Debian 12.": "%s 17 é suportado apenas no Debian 12.",
    "(What Does this Mean?)": "(O que isso significa?)",
    "Additionally, nodejs* packages are held to prevent upgrades to newer Node.js versions that may break %s components that depend on a specific Node.js runtime.": "Além disso, os pacotes nodejs* são retidos para evitar atualizações para versões mais novas do Node.js que possam quebrar componentes do %s que dependem de uma versão específica.",
    "Administrator User": "Usuário Administrador",
    "Affected files:": "Arquivos afetados:",
    "Automatic Module Security Updates": "Atualizações Automáticas de Segurança de Módulos",
    "Automatic Module Updates": "Atualizações Automáticas de Módulos",
    "Automatic System Updates": "Atualizações Automáticas do Sistema",
    "Between 12pm and 4pm": "Entre 12h e 16h",
    "Between 4am and 8am": "Entre 4h e 8h",
    "Between 4pm and 8pm": "Entre 16h e 20h",
    "Between 8am and 12pm": "Entre 8h e 12h",
    "Between 8pm and Midnight": "Entre 20h e 0h",
    "Between Midnight and 4am": "Entre 0h e 4h",
    "Broken:": "Quebrado:",
    "Cache refreshed successfully.": "Cache atualizado com sucesso.",
    "Cannot Connect to Asterisk": "Não foi possível conectar ao Asterisk",
    "Check for Updates every": "Verificar atualizações a cada",
    "Click to expand": "Clique para expandir",
    "Conflicts": "Conflitos",
    "Copyright &copy; %s Motocar": "Copyright &copy; %s Motocar",
    "Current PBX Version:": "Versão Atual do PABX:",
    "Current System Version:": "Versão Atual do Sistema:",
    "Current Version": "Versão Atual",
    'Custom Goto contexts must contain the string "custom-".  ie: custom-app,s,1': 'Contextos Goto personalizados devem conter "custom-". Ex.: custom-app,s,1',
    "Day": "Dia",
    "Disabled:": "Desabilitado:",
    "Email Address:": "Endereço de E-mail:",
    "Email Body": "Corpo do E-mail",
    "Email Only": "Somente E-mail",
    "Email Subject": "Assunto do E-mail",
    "Enabled:": "Habilitado:",
    "Enter a valid email address": "Informe um endereço de e-mail válido",
    "Enter an identifier for this machine": "Informe um identificador para esta máquina",
    "Error loading system updates data.": "Erro ao carregar dados de atualizações do sistema.",
    "Error refreshing cache.": "Erro ao atualizar cache.",
    "Failed to refresh cache.": "Falha ao atualizar cache.",
    "Force Install": "Forçar Instalação",
    "Force Update": "Forçar Atualização",
    "Friday": "Sexta-feira",
    "Held Packages": "Pacotes Retidos",
    "Initial Setup": "Configuração Inicial",
    "Keep Nav Bar Expanded": "Manter Barra de Navegação Expandida",
    "Last online check:": "Última verificação online:",
    "Loading system updates data...": "Carregando dados de atualizações do sistema...",
    "Locally chosen FreePBX module from your system": "Módulo selecionado localmente do seu sistema",
    "Module Updates": "Atualizações de Módulos",
    "Modules with Upgrades:": "Módulos com Atualizações:",
    "Monday": "Segunda-feira",
    "MotocarPABX": "MotocarPABX",
    "Nav. Bar is always shown by default or not.": "Define se a barra de navegação é exibida sempre expandida por padrão.",
    "Needs Upgrade:": "Precisa de Atualização:",
    "New Version": "Nova Versão",
    "No held packages found.": "Nenhum pacote retido encontrado.",
    "No repository files found.": "Nenhum arquivo de repositório encontrado.",
    "No security upgradable packages found.": "Nenhum pacote com atualização de segurança encontrado.",
    "No upgradable packages found.": "Nenhum pacote atualizável encontrado.",
    "Notice: System Upgrade (%s) available!": "Aviso: Atualização do Sistema (%s) disponível!",
    "Notifications Email address": "Endereço de e-mail para notificações",
    "Package Name": "Nome do Pacote",
    "Please execute": "Por favor, execute",
    "Please provide the core settings that will be used to administer and update your system": "Informe as configurações principais que serão usadas para administrar e atualizar o sistema",
    'Please select a "Destination"': 'Por favor, selecione um "Destino"',
    "Please update your repository configuration to use 'bookworm' instead of 'stable' to prevent unsupported upgrades.": "Atualize a configuração do seu repositório para usar 'bookworm' em vez de 'stable' para evitar atualizações não suportadas.",
    "Refresh Cache": "Atualizar Cache",
    "Refresh cache to get latest data": "Atualizar cache para obter os dados mais recentes",
    "Refreshing...": "Atualizando...",
    "Repository": "Repositório",
    "Repository Configuration Files": "Arquivos de Configuração do Repositório",
    "Restart": "Reiniciar",
    "Saturday": "Sábado",
    "Scheduler and Alerts": "Agendador e Alertas",
    "Security Updates": "Atualizações de Segurança",
    "Security Upgradable Packages": "Pacotes com Atualizações de Segurança",
    "Send Security Emails For Unsigned Modules": "Enviar E-mails de Segurança para Módulos Não Assinados",
    "Set email Subject": "Definir assunto do e-mail",
    "Set email body": "Definir corpo do e-mail",
    "Set email type": "Definir tipo do e-mail",
    "Setup System": "Configurar Sistema",
    "Some of the recently updated modules needs apache service to restart to work properly, so please restart the apache service.": "Alguns dos módulos atualizados recentemente exigem o reinício do serviço Apache para funcionar corretamente.",
    "Summary": "Resumo",
    "Sunday": "Domingo",
    "Sysadmin Module Notice": "Aviso do Módulo Sysadmin",
    "System Identification": "Identificação do Sistema",
    "System Identifier": "Identificador do Sistema",
    "System Identifier:": "Identificador do Sistema:",
    "System Notifications Email": "E-mail de Notificações do Sistema",
    "System OS Updates Summary": "Resumo de Atualizações do Sistema Operacional",
    "System Updates": "Atualizações do Sistema",
    "System Upgrades Available:": "Atualizações de Sistema Disponíveis:",
    "System update functionality is only supported with Sysadmin module.": "A funcionalidade de atualização do sistema requer o módulo Sysadmin.",
    "System updates are Operating-system level updates, such as the Linux Kernel, Asterisk, and the Apache Web Server. Module updates are parts of %s, such as IVR, Ring Groups, or Queues. Security updates will <strong>always</strong> be automatically installed. It is recommended that both are left on.<br />Note that updates <strong>do not cause an outage</strong>. Some may require a reboot to be applied, and you will be told this in the summary email.": "Atualizações do sistema são atualizações no nível do sistema operacional, como Kernel Linux, Asterisk e Apache. Atualizações de módulos são partes do %s, como URA, Grupos de Chamada ou Filas. Atualizações de segurança serão <strong>sempre</strong> instaladas automaticamente. Recomenda-se manter ambas ativadas.<br />Observe que as atualizações <strong>não causam interrupção</strong>. Algumas podem exigir reinicialização, o que será informado no e-mail de resumo.",
    "System updates via the web interface are not currently available.": "Atualizações do sistema pela interface web não estão disponíveis no momento.",
    "The freepbx17 and sangoma-pbx17 Debian packages are bootstrap-only components. Their installation process is non-idempotent, and reinstalling them will overwrite critical configuration and may render the system unusable. For this reason, these packages are held to prevent accidental reinstallation.": "Os pacotes Debian freepbx17 e sangoma-pbx17 são componentes apenas de inicialização e ficam retidos para evitar reinstalação acidental que sobrescreveria configurações críticas.",
    "The numbers below may be inaccurate if new modules have been released since the last check:": "Os números abaixo podem estar desatualizados se novos módulos tiverem sido lançados após a última verificação:",
    "This module has conflicts that may cause system issues": "Este módulo possui conflitos que podem causar problemas no sistema",
    "Thursday": "Quinta-feira",
    "To automatically prevent Debian 13 upgrades:": "Para impedir automaticamente atualizações para o Debian 13:",
    "To prevent this, ensure your repository files use a specific Debian codename (such as 'bookworm') instead of 'stable'.": "Para evitar isso, garanta que os arquivos de repositório usem o codinome específico do Debian (como 'bookworm') em vez de 'stable'.",
    "Total Module Count:": "Total de Módulos:",
    "Tuesday": "Terça-feira",
    "Type of email": "Tipo de e-mail",
    "Unable to load system updates data.": "Não foi possível carregar os dados de atualizações do sistema.",
    "Updates": "Atualizações",
    "Upgradable Packages": "Pacotes Atualizáveis",
    "Use": "Usar",
    "View": "Visualizar",
    "Vulnerable to security issues %s": "Vulnerável a problemas de segurança %s",
    "Vulnerable, Requires: %s": "Vulnerável, Requer: %s",
    "WARNING: Debian 13 Upgrade Risk Detected": "AVISO: Risco de Atualização para Debian 13 Detectado",
    "WARNING: Javascript is disabled in your browser. The %s administration interface requires Javascript to run properly. Please enable javascript or switch to another  browser that supports it.": "AVISO: O JavaScript está desabilitado no seu navegador. A interface de administração do %s requer JavaScript para funcionar corretamente. Habilite o JavaScript ou utilize outro navegador compatível.",
    "We are unable to find any information on the module you are looking for.": "Não foi possível encontrar informações sobre o módulo solicitado.",
    "We hope you enjoy using %s": "Esperamos que você aproveite o %s",
    "We strongly suggest that you re-enable your Dashboard module through one of the following links:": "Recomendamos fortemente que você reabilite o módulo Painel por meio de um dos links abaixo:",
    "Wednesday": "Quarta-feira",
    "Welcome to ": "Bem-vindo ao ",
    "Welcome to %s": "Bem-vindo ao %s",
    "Welcome to %s!": "Bem-vindo ao %s!",
    "Why are packages held?": "Por que os pacotes ficam retidos?",
    "You are attempting to load licensed modules without a proper Zend Guard Configuration. Please ensure you have Zend Guard installed on your system and have downloaded a license via the System Administration module.": "Você está tentando carregar módulos licenciados sem uma configuração válida do Zend Guard.",
    "You are attempting to modify settings from a URL that does not appear to have come from a FreePBX page link or button. This can occur if you manually typed in the URL below. This action has been blocked because the HTTP_REFERER does not match your current SERVER. If you require this access, you can set Check Server Referrer=false in Advanced Settings to disable this security check": "Você está tentando modificar configurações a partir de uma URL que não veio de um link ou botão válido do painel. Essa ação foi bloqueada por segurança porque o HTTP_REFERER não corresponde ao servidor atual.",
    "You have some broken %s Modules. We advise you take care of these as soon as possible: ": "Você possui alguns módulos do %s com falha. Recomendamos corrigi-los o quanto antes: ",
    "You may wish to redownload this module if the data is corrupted.": "Talvez seja necessário baixar este módulo novamente se os dados estiverem corrompidos.",
    "Your browser is out-of-date!": "Seu navegador está desatualizado!",
    "Your repository configuration may allow an upgrade to Debian 13, which is not supported by %s.": "A configuração do seu repositório pode permitir atualização para o Debian 13, que não é suportado pelo %s.",
    "Zend Mis-Configuration": "Configuração Incorreta do Zend",
    "and": "e",
    "confirm email": "confirmar e-mail",
    "email address": "endereço de e-mail",
    "on the command line.": "na linha de comando.",
    "to run sysadmin hook": "para executar o hook do sysadmin",
}

DASH_TRANSLATIONS = {
    "%s Statistics": "Estatísticas de %s",
    "%s messages are queued on this machine, and have not been delivered": "%s mensagens estão na fila desta máquina e não foram entregues",
    "1 message is queued on this machine, and have not been delivered": "1 mensagem está na fila desta máquina e não foi entregue",
    "<strong>'%s'</strong>": "<strong>'%s'</strong>",
    "Add a note": "Adicionar nota",
    "An error occured": "Ocorreu um erro",
    "Available space details": "Detalhes de espaço disponível",
    "Dashboard Module": "Módulo Painel",
    "Deleted note": "Nota excluída",
    "Disable collection of system statistics": "Desabilitar coleta de estatísticas do sistema",
    "Display firewall status": "Exibir status do firewall",
    "Expiry time for system statistics": "Tempo de expiração das estatísticas do sistema",
    "Live Network Usage": "Uso de Rede em Tempo Real",
    "Loading Interface %s...": "Carregando Interface %s...",
    "Mail Queue": "Fila de E-mail",
    "Message for the request": "Mensagem da solicitação",
    "Missing Class Object!": "Objeto de classe ausente!",
    "No notes found": "Nenhuma nota encontrada",
    "Notepad": "Bloco de Notas",
    "Notes": "Notas",
    "Read the System licence information": "Ler informações de licença do sistema",
    "Returns storage id": "Retorna o ID do armazenamento",
    "Save": "Salvar",
    "Saved note": "Nota salva",
    "Set the maximum age in seconds before system statistics are refreshed. The minimum value is 50 seconds.": "Define o tempo máximo em segundos antes de atualizar as estatísticas do sistema. O mínimo é 50 segundos.",
    "Set this to true to prevent persistent collection of system statistics such as CPU, memory, and channel usage.": "Defina como verdadeiro para impedir a coleta contínua de estatísticas do sistema como CPU, memória e uso de canais.",
    "Sorry, unable to find any diskspace": "Não foi possível localizar informações de espaço em disco",
    "Status for the request": "Status da solicitação",
    "Successfully found disks space details": "Detalhes de espaço em disco obtidos com sucesso",
    "The Dashboard will display a warning when the PBX Firewall is disabled. When this is set to 'no', the Dashboard warning will be permanently suppressed.": "O Painel exibirá um aviso quando o Firewall do PABX estiver desabilitado. Ao definir como 'não', o aviso será suprimido permanentemente.",
    "Use to get all the diskspace": "Usado para obter todo o espaço em disco",
    "disk total size details": "detalhes do tamanho total do disco",
    "disk used percentage": "percentual de uso do disco",
    "storage path details": "detalhes do caminho de armazenamento",
    "used space details": "detalhes do espaço utilizado",
}


def po_unescape(s: str) -> str:
    return ast.literal_eval('"' + s + '"')


def po_escape(s: str) -> str:
    return (
        s.replace("\\", "\\\\")
        .replace('"', '\\"')
        .replace("\n", "\\n")
        .replace("\t", "\\t")
    )


def update_and_compile_po(po_path: Path, mo_path: Path, extra_translations: dict[str, str]) -> tuple[int, int]:
    text = po_path.read_text(encoding="utf-8")
    blocks = re.split(r"\n{2,}", text.strip())
    updated_blocks = []
    seen_ids = set()
    catalog: dict[bytes, bytes] = {}
    replaced_count = 0

    for block in blocks:
        lines = block.splitlines()
        is_fuzzy = any(l.startswith("#,") and "fuzzy" in l for l in lines)
        msgid_parts = []
        msgid_plural_parts = []
        msgstr_parts = []
        plural_strs: dict[int, list[str]] = {}
        mode = None
        current_idx = 0

        for line in lines:
            if line.startswith("#") or not line.strip():
                continue
            if line.startswith("msgid_plural "):
                mode = "plural"
                msgid_plural_parts.append(line[14:-1])
            elif line.startswith("msgid "):
                mode = "id"
                msgid_parts.append(line[7:-1])
            elif line.startswith("msgstr["):
                m = re.match(r"msgstr\[(\d+)\]\s+\"(.*)\"$", line)
                if m:
                    mode = "pstr"
                    current_idx = int(m.group(1))
                    plural_strs.setdefault(current_idx, []).append(m.group(2))
            elif line.startswith("msgstr "):
                mode = "str"
                msgstr_parts.append(line[8:-1])
            elif line.startswith('"') and line.endswith('"'):
                chunk = line[1:-1]
                if mode == "id":
                    msgid_parts.append(chunk)
                elif mode == "plural":
                    msgid_plural_parts.append(chunk)
                elif mode == "str":
                    msgstr_parts.append(chunk)
                elif mode == "pstr":
                    plural_strs.setdefault(current_idx, []).append(chunk)

        msgid_raw = "".join(msgid_parts)
        msgid = po_unescape(msgid_raw) if msgid_parts else ""
        seen_ids.add(msgid)

        if not msgid_plural_parts and msgid in extra_translations:
            msgstr = po_unescape("".join(msgstr_parts)) if msgstr_parts else ""
            if not msgstr or is_fuzzy:
                new_val = extra_translations[msgid]
                new_lines = [l for l in lines if not (l.startswith("#,") and "fuzzy" in l)]
                # Rebuild block preserving comments
                comments = [l for l in new_lines if l.startswith("#")]
                block_lines = comments + [
                    f'msgid "{po_escape(msgid)}"',
                    f'msgstr "{po_escape(new_val)}"',
                ]
                block = "\n".join(block_lines)
                msgstr = new_val
                is_fuzzy = False
                replaced_count += 1
        else:
            msgstr = po_unescape("".join(msgstr_parts)) if msgstr_parts else ""

        updated_blocks.append(block)

        if is_fuzzy:
            continue

        if msgid_plural_parts:
            plural_id = po_unescape("".join(msgid_plural_parts))
            forms = [po_unescape("".join(plural_strs[i])) for i in sorted(plural_strs)]
            if any(forms):
                catalog[(msgid + "\x00" + plural_id).encode("utf-8")] = "\x00".join(forms).encode("utf-8")
        else:
            if msgid == "" or msgstr:
                catalog[msgid.encode("utf-8")] = msgstr.encode("utf-8")

    # Add missing msgids that were not present in the .po file at all
    added_count = 0
    for msgid, msgstr in extra_translations.items():
        if msgid not in seen_ids:
            updated_blocks.append(f'msgid "{po_escape(msgid)}"\nmsgstr "{po_escape(msgstr)}"')
            catalog[msgid.encode("utf-8")] = msgstr.encode("utf-8")
            added_count += 1

    po_path.write_text("\n\n".join(updated_blocks) + "\n", encoding="utf-8")

    # Write GNU gettext .mo binary (little-endian)
    keys = sorted(catalog.keys())
    offsets = []
    ids_buf = bytearray()
    strs_buf = bytearray()
    for k in keys:
        v = catalog[k]
        offsets.append((len(ids_buf), len(k), len(strs_buf), len(v)))
        ids_buf.extend(k + b"\x00")
        strs_buf.extend(v + b"\x00")

    header_size = 28
    table_size = 8 * len(keys)
    ids_start = header_size + table_size * 2
    strs_start = ids_start + len(ids_buf)

    key_table = bytearray()
    val_table = bytearray()
    for id_off, id_len, str_off, str_len in offsets:
        key_table.extend(struct.pack("<II", id_len, ids_start + id_off))
        val_table.extend(struct.pack("<II", str_len, strs_start + str_off))

    mo_header = struct.pack(
        "<IIIIIII",
        0x950412DE,
        0,
        len(keys),
        header_size,
        header_size + table_size,
        0,
        0,
    )
    mo_path.write_bytes(mo_header + bytes(key_table) + bytes(val_table) + bytes(ids_buf) + bytes(strs_buf))
    return replaced_count, added_count


if __name__ == "__main__":
    r1, a1 = update_and_compile_po(AMP_PO, AMP_MO, AMP_TRANSLATIONS)
    r2, a2 = update_and_compile_po(DASH_PO, DASH_MO, DASH_TRANSLATIONS)
    print(f"amp.mo compilado: {r1} preenchidas, {a1} adicionadas")
    print(f"dashboard.mo compilado: {r2} preenchidas, {a2} adicionadas")
