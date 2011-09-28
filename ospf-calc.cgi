#!/usr/bin/perl

use CGI;
$q = new CGI;

if ($q->param('source'))
{
    print $q->header("text/plain; charset=EUC-JP");
    print "\n";
    open(SRC, $0);
    print <SRC>;
    exit 0;
}

################################################################
# �إå�
################################################################
$title = 'OSPF ��ϩ�׻�������';
$version = '2009/12/14 ����';
$mail = 'kashima@jp.fujitsu.com';


$mailto = $q->a({-href => "mailto:$mail"}, $q->i($mail));

sub description
{
    # print $q->style('p { width: 50%;  text-indent: 1em; }');
    print $q->h3('����');
    print $q->p
	('OSPF �ǥȥ�֥�ˤʤ꤬���ʤ��ȤȤ��ơ�'
	 . '�ֲ��Τ��η�ϩ�Ϥ��������������Ƥ��ޤ������'
	 . '�Ȥ���������������ʤ��Ȥ�����������ޤ���'
	 . 'OSPF �η�ϩ�׻����Ȥ��˥��ꥢ��η�ϩ�׻��ϡ�'
	 . 'RIP �� BGP �Ȱ�äƥ٥��ȥ뷿�ǤϤʤ�����'
	 . '�ǡ�����ή��Ƥ��������ȷ�ϩ�Ȥ�ɬ��������פ��ޤ���'
	 . '��ǧ���褦�ˤ⡢���å��� RFC ����ˤ��äƤ��ޤ�޲��ʤ��Τǡ�'
	 . '��ñ�˳�ǧ���뤳�Ȥ��Ǥ��ޤ���');
    print $q->p
	('�����ǡ�����Ȥʤ��ϩ�ޤǤΥѥ���޼��Ǥ���Сġ��Ȥ���ư����'
	 . '���Υץ�����񤭻Ϥ�ޤ�����');
    print $q->p
	('��ǰ�ʤ��� Ajax �ʤɤΥ����ʥߥå��ʲ��̤ˤĤ��Ƥ褯�Τ�ʤ��Τǡ�'
	 . '�Τʤ���� HTML �ˤ���������ߥƥ����ȤǺ������Ƥ��ޤ�����'
	 . '��󥯤򤿤ɤ뤳�Ȥ� LSA ��ʤ������ä��ꤹ�뤳�Ȥ�'
	 . '��ǽ�ˤ��Ƥ��ޤ���');

    print $q->h3('�оݤȤʤ�롼������');
    print $q->p('�ʲ������֤���� show ip ospf database detail �ˤĤ���'
		. '���Ϥμ��Ӥ�����ޤ���');
    print $q->ul($q->li('GeoStream R900 ���꡼��'),
		 $q->li('Si-R 3400 (��¬)'),
		 $q->li('IPCOM S1000 ��'),
		 $q->li('IPCOM S2000 ��'),
		 $q->li('IPCOM EX ��'));
    print $q->p('�ޤ���ɽ���Ϥλ��Ƥ���롼�����֤ˤ��ǡ����Ǥ�'
		. '����ץ뤬����Ф������٤β��Ϥ���ǽ�Ǥ���'
		. '�ɲ��б��Τ���˾�ϡ�show ip ospf database �ξܺ�'
		. '(LSA �������ξ���ޤǴޤ���) ��'
		. $mailto
		. '�ޤǤ����꤯����������ֶ�̳�Ǥ��Τ�ȿ�Ǥ��٤��Ǥ���'
		. '���ä��б�����ΤǤϤʤ������Ȼפ��ޤ���');

    print $q->h3('�Ȥ���');
    print $q->p('�ʲ������Τ����֤� OSPF Router-ID ���ǧ���Ƥ���������');
    print $q->ol($q->li('show ip ospf'));
    print $q->blockquote($q->pre("Statistics and variables:\n"
				 . "  Router ID: 1.1.1.0\n"
				 . "  SPF calculated 39 times"));
    print $q->p('�������ä�������ɽ�����ФƤ���С�'
		. 'Router ID ����ʬ���������֤� OSPF Router-ID �Ǥ���');
    print $q->p('�ޤ����ʲ������Τ����֤� OSPF �ǡ����١�����'
		. '�ե�����˼������Ƥ���������');
    print $q->ol($q->li('UNIX �� Linux �ʤ� script ���ޥ�ɡ�'
			. 'TeraTerm �ʤ�����������ä���ǽ��'
			. '�롼�����֤���ν��Ϥ�ƥ�������¸�Ǥ���褦��'
			. '���Ƥ�������'),
		 $q->li('script ���ޥ�ɤ���Ѥ��Ƥ�����ϡ�'
			. '������Υ����뤫�饿�����åȥ롼����'
			. '�����󤷤Ƥ�������'),
		 $q->li('"show ip ospf database detail" ��¹Ԥ��Ƥ�������'),
		 $q->li('���Ϥ��줿���Ƥ� 1 �ԤŤĤǤϤʤ�'
			. 'LSA �μ�����ˤ������͡��ʾ������ä�'
			. '���뤳�Ȥ��ǧ���Ƥ���������'));
    print $q->p('�����Ǽ��������ե�������ܥڡ����Ρֻ��ȡץܥ����'
		. '���åץ��ɤǤ���褦�ˤ��Ƥ���������'
		. '�ޤ������Ʊ���ˡ��ǽ�˼������� OSPF Router-ID ��'
		. '���Υ��ޤ˵��������Ǹ�ˡַ׻��ץܥ���򲡤��Ƥ���������');
    print $q->blockquote('(�ʤ��������Ȥˤ���Ȥ��ꡢshow ip ospf �ν��Ϥ�'
			 . '���åץ��ɤ���ե�����˴ޤ�뤳�Ȥ��ǽ�Ǥ���'
			 . '���ξ��� Router-ID �������Ϥ���ɬ�פ�'
			 . '����ޤ���');
    print $q->p('��������ȼ��β��̤ˤϡ���ϩ�׻��η�̤ȡ�'
		. '�����롼���˶ᤤ�������� LSA ��ɽ������Ƥ���'
		. '�Ȼפ��ޤ���');
    print $q->p('��ϩɽ���鵤�ˤʤ��ϩ��õ�����顢'
		. '�֤ҤȤ����ץ���å��ǡ����ΰ��褫��롼���ޤǤ�'
		. '�ѥ���é�뤳�Ȥ��Ǥ��ޤ���'
		. '�ޤ���ͭ���ˤʤ�ʤ��ä���ϩ�Ⱦ��֤���Ӥ����ꡢ'
		. '���η�ϩ��ѥ���η�ϩ�θ��ˤʤ� LSA ��Ĵ�٤뤳�Ȥ�'
		. '�Ǥ��ޤ���');
    print $q->p('�ޤ���LSDB ���鵤�ˤʤ� LSA �򥯥�å����ơ�'
		. '���� LSA ����̣�����ϩ�䡢�����ޤǤΥ����Ȥʤɤ�'
		. '�Τ뤳�Ȥ�Ǥ��ޤ���'
		. 'Router-LSA �Υ�󥯾���򥯥�å�����С���������ɤ�'
		. '�롼���䥵�֥ͥåȤ˷Ҥ��äƤ���Τ�ʬ����ޤ���'
		. 'Network-LSA �Υ�󥯾���򥯥�å�����С����Ϥˤɤ�'
		. '�롼��������Τ�ʬ����ޤ���');

    print $q->h3('�Ǹ��');

    print $q->p('���� Web �ڡ����ϡ��ץ����ˤ����������ʳ�ȯʪ�Ǥ�'
		. '����ޤ��󡣤��Υڡ��������Ѥ���ˤ����äơ�'
		. '�桼����Ͽ������������פǤ�����'
		. '���Υڡ����ν������ƤˤĤ����ݾڤϤǤ��ޤ���'
		. '(�����񤯤Τ��ᤷ���Ǥ����������ʳ�ȯʪ�ǤϤʤ��Τ�'
		. '��������ޤ���)��');
    print $q->p('���� Web �ڡ����ˤĤ��ƤΤ��ո��䤴��˾�ˤĤ��Ƥ�'
		. $mailto
		. '�ޤǤ�Ϣ��������');
}

@history=('2009/12/10: ��ϩ�׻��ޤǴ�λ',
	  '2009/12/14: �׻���̤����ܸ��������ä�����',
	  '2009/12/14: <a href �������򤭤���ȼ�����褦ʸ���� <br> ����',
	  '2009/12/14: �֤ҤȤĿʤ�פȡ֤ҤȤ����פǷ�ϩ�� LSA �����ä���ˤʤ�ʤ��褦�ˤ��� (AS �����롼����ϩ�˰�¸���� AS ������ϩ���оݳ�)',
	  '2009/12/16: External path preference ����ͤǤϤʤ����դˤ���',
	  '2009/12/16: Forwarder �׻��ߥ�����',
	  );
@todo=('RouterID ���ϥե�����ɤ��Ѥ��ͤ�����ʤ��褦 javascript ���������椹��',
# 12/16       'External/NSSA �� Forwarder ����Υѥ�����γ�ǧ'
       '��������Τ��ᡢ���Υڡ����μ�ݤʤɤ򵭺ܤ���',
       '��������Ϥ��Ƥ��äơ�javascript ��Ŭ�ڤʰ�������Ф��Ƥ��С���������֤��ä����פ� traceroute �ε�é�꤬��ǽ�ʤ󤸤�͡�',
       '���ѥ��󥱡��Ȥ��ߤ���',
       '���ո�����˾�Υڡ������ꤿ��',
       );
@thanksto=('���Ȥ���: ��������ˤ����äơ��͡��ʥ��ɥХ�����ĺ���ޤ���');

sub show_and_exit
{
    my ($desc, @list) = @_;
    print $q->start_ul;
    for $txt (@list)
    {
	print $q->li($q->escapeHTML($txt));
    }
    print $q->end_ul;
    print $q->end_html;
    exit 0;
}

print $q->header('text/html; charset=EUC-JP');
print $q->start_html(-title => $title)."\n";
print $q->start_div({-id => 'head'})."\n";
print $q->comment('header')."\n";
print $q->h1($title)."\n";
print $q->i($version)."\n";
print $q->br, $mailto, $q->br, "\n";
print $q->a({-href => $q->url(-relative => 1)}, '�����')."\n";

################################################################
# ��¤�Υ���̾
################################################################
$Name = 'Name';           # String # <a name �� <a href �Ѥ�̾��
$Text = '�ƥ�����';       # String # ���ϥե�����ʸ��
$Invalid = '�Բ���ͳ';    # String # �ԲĤǤ�����ͳ
$Mask = '�ͥåȥޥ���';   # String # �ͥåȥޥ���
$Area = '���ꥢ';         # String # ���ꥢ ID
$AreaVal = '���ꥢ��';    # int    # ���ꥢ ID ����Ͳ�������� (��������)
$LSType = 'LSType';       # String # LSA ����
$LSId = 'LSId';           # String # Link State ID
$AdvRtr = 'ȯ�Ը�LSA';    # String # LSA ���󸵥롼���� �롼�� ID
$Age = '��';              # int    # LS Age 0��3599, ��(3600)
$Opt = 'Option';          # String # ���ץ����
$RtrOpt = '�롼��Opt';    # String # Router-LSA ��ͭ���ץ����
$Pri = 'ͥ����';          # int    # LSA ���ϩ��ͥ����
$Metric = '���ܥ�����';   # int    # LSA �� Link �˵��ܤ��줿������
$Cost = '�ѥ�������';     # int    # �ѥ����ΤΥ�����
$Link = '���';         # ARRAY  # Router/Network-LSA �� Link
$Gateway = '���ۥå�';    # HASH   # ���ۥå׷� (���ɥ쥹 => $Name)
$Route = '��ϩ';          # Object # LSA ��������ϩ
$ASBR = 'AS�����롼��';   # Object # LSA ������ AS �����롼����ϩ
$Back = '�ҤȤ����';     # ARRAY  # ���ʤ� LSA �ޤ��� RT
$More = '�ҤȤĿʤ�';     # ARRAY  # ���ʤ� LSA �ޤ��� RT
$BackLink = '�ե��';   # bool   # ����󥯤ˤʤäƤ뤳�Ȥ򼨤��ե饰
$Stub = '��ü��ϩ';       # Object # Router-LSA �� Stub Link �ˤ���ϩ
$MyAddr='��¦���ɥ쥹';   # Str    # �롼�����ȤΥ��ɥ쥹
$MyIfp = '��¦ifIndex';   # String # �롼���� ifIndex
$Root = 'SPF����';        # bool   # SPF �׻������򼨤��ե饰
$Peer = 'SPF���ۥå�';    # bool   # SPF �׻��Ǽ��ۥåפ򼨤��ե饰
$LinkBackOk =
    'LinkBackOk';         # bool   # �����������Ω�򼨤��ե饰
$MaybeTransit = '�ȥ�󥸥å�'.
    '���ꥢ���ޥ�';       # bool   # �ȥ�󥸥åȥ��ꥢ���ޥ�
$ExtOpt = 'AS����Type';   # String # External/NSSA-LSA ��ͭ���ץ����
$Forward='ž�����ɥ쥹';  # Str    # ž���襢�ɥ쥹
$ExtPref= '�ѥ�ͥ����';   # int    # External path preference (Section 16.4.1)
$Type1Cost =
    'Type1������';        # int    # Type2 ������ϩ�� Type1 ������
$HasForwarder =
    'Forwarderͭ';        # bool   # �ե���������뤳�Ȥ򼨤�
$OnTree = 'OnTree';       # bool   # LSDB �����ߺѤ򼨤��ե饰
$Addr = '���襢�ɥ쥹';   # String # ��ϩ�ΰ��襢�ɥ쥹
$LSA = '����LSA';         # Object # LSA
$Valid = 'ͭ��';          # bool   # ͭ���Ǥ��뤳�Ȥ򼨤��ե饰

################################################################
# �桼�ƥ���ƥ��ѿ�
################################################################

# ��ʬ���Ȥ򼨤�������
$SelfCost = '����(���äƼ�ʬ���Ȥ����)';

# ��ϩ��ͥ����ɽ
%rtpri = ('Network' => 2,
	  'Router' => 3,
	  'Stub' => 4,
	  'SumNet' => 5,
	  'ASBR' => 7,
	  'External' => 8,
	  'NSSA' => 8);

# ��ϩ�μ���ɽ
%rtype = ('Network' => '�ͥåȥ�����ɥ쥹',
	  'Router' => '�롼��ID',
	  'Stub' => '�ͥåȥ�����ɥ쥹',
	  'SumNet' => '�ͥåȥ�����ɥ쥹',
	  'External' => '�ͥåȥ�����ɥ쥹',
	  'NSSA' => '�ͥåȥ�����ɥ쥹',
	  'ASBR' => 'AS�����롼��');

# rfc2328 16.4.1 External Path preference
%extpref = ('����' => 1,
	    '����' => 2);

# LSA ������
%lsadesc = ('Router' => '���ꥢ��Υ롼��',
	    'Network' => '���ꥢ��ͥåȥ��',
	    'Stub' => '���ꥢ�����ü�ͥåȥ��',
	    'SumNet' => '���ꥢ���ͥåȥ��',
	    'SumRtr' => '���ꥢ���� AS �����롼��',
	    'External' => 'AS������ϩ',
	    'NSSA' => 'AS������ϩ(NSSA���ꥢ��)');

# mask ���� masklen
@masklen = ('0.0.0.0',
	    '128.0.0.0',
	    '192.0.0.0',
	    '224.0.0.0',
	    '240.0.0.0',
	    '248.0.0.0',
	    '252.0.0.0',
	    '254.0.0.0',
	    '255.0.0.0',
	    '255.128.0.0',
	    '255.192.0.0',
	    '255.224.0.0',
	    '255.240.0.0',
	    '255.248.0.0',
	    '255.252.0.0',
	    '255.254.0.0',
	    '255.255.0.0',
	    '255.255.128.0',
	    '255.255.192.0',
	    '255.255.224.0',
	    '255.255.240.0',
	    '255.255.248.0',
	    '255.255.252.0',
	    '255.255.254.0',
	    '255.255.255.0',
	    '255.255.255.128',
	    '255.255.255.192',
	    '255.255.255.224',
	    '255.255.255.240',
	    '255.255.255.248',
	    '255.255.255.252',
	    '255.255.255.254',
	    '255.255.255.255');
for ($i = 0;  $i < $#masklen;  ++$i)
{
    $masklen{$masklen[$i]} = $i;
}

################################################################
# ���åץ��ɤ��줿 show ip ospf database detail ���ɤ߹���
################################################################
sub lsaname # LSA ���̻�
{
    my ($area, $type, $id, $rtr) = @_;
    "Area:$area " . join(':', $type, $id, $rtr);
}
sub rtdest # ��ϩ����
{
    my ($type, $dest, $areamask) = @_;
    my ($rtype) = ($rtype{$type});
    if ($rtype eq '�ͥåȥ�����ɥ쥹')
    {
	return "$rtype:$dest:$areamask";
    }
    if ($rtype eq '�롼��ID')
    {
	return "$rtype:$dest Area:$areamask";
    }
    return "$rtype:$dest";
}
sub rtname # ��ϩ���̻�
{
    my ($type, $dest, $areamask, $lsa) = @_;
    join(':', $type, $dest, $areamask, $lsa->{$Name});
}
sub addrval
{
    my ($addr) = @_;
    my (@addr, $val, $i);
    @addr = split(/\./, $addr);
    $val = 0;
    for ($i = $[;  $i <= $#addr;  ++$i)
    {
	$val = ($val * 0x100) + $addr[$i];
    }
    $val;
}
if ($q->param('db'))
{
    $self = $q->param('routerid');
    $text = $q->upload('db');
    $rfc1583compat = $q->param('RFC1583Compat');
    $debug = $q->param('debug');

    while (<$text>)
    {
	# �롼��ID�γ�ǧ
	unless ($self)
	{
	    if (/[Ss]tatistics and variables:/o)
	    {
		$nextwillberouterid = 1;
		next;
	    }
	    if ($nextwillberouterid)
	    {
		if (/Router ID: (\d+\.\d+\.\d+\.\d+)/o)
		{
		    $self = $1;
		}
		$nextwillberouterid = undef;
		next;
	    }
	}

	# show ip ospf database detail �Υ��ꥢ��������ɤ߹���
	if (/^LSA list in the LSDB for area (\d+\.\d+\.\d+\.\d+)/o)
	{
	    ($area) = ($1);
	    $area{$area} = 0;
	    $areaval = &addrval($area);
	    next;
	}
	if (/^LSA list in the LSDB/o)
	{
	    $area = 'Global';
	    $area{$area} = 0;
	    $areaval = 0x100000000;
	    next;
	}

	# LSA �����
	if (/^(Router|Network|SumNet|SumRtr|External|NSSA)\s+Id\s+(\d+\.\d+\.\d+\.\d+)\s+Router\s(\d+\.\d+\.\d+\.\d+)/o)
	{
	    ($lstype, $lsid, $adv) = ($1, $2, $3);
	    # $area �����Ԥ����³����
	    # $lsa �Ͽ�������
	    $name = &lsaname($area, $lstype, $lsid, $adv);

	    $lsa = {};
	    $lsa->{$Text} = $_;
	    $lsa->{$Name} = $name;
	    $lsa->{$Gateway} = {};
	    $lsa->{$Back} = [];
	    $lsa->{$More} = [];

	    $lsa->{$Area} = $area;
	    $lsa->{$LSType} = $lstype;
	    $lsa->{$LSId} = $lsid;
	    $lsa->{$AdvRtr} = $adv;
	    $lsdb{$name} = $lsa;
	    next;
	}

	# LSA 2����
	if (/^Age\s+(\d+)\s+Seq\s+[\dA-Fa-f]+\s+Sum\s+[\dA-Fa-f]+\s+Length\s+\d+\s+Option\s+<([^<>]*)>/o)
	{
	    ($age, $opt) = ($1, $2);
	    # $lsa, $area, $lsid �Ϸ�³����

	    $lsa->{$Text} .= $_;
	    $lsa->{$Age} = int($age);
	    $lsa->{$Opt} = $opt;

	    # Network-LSA �� Id ��ʣ�ϡ�Age ����Ӥ��뤿��
	    # lsdb ���ü����Ͽ���äƤ���
	    if ($lstype eq 'Network')
	    {
		$name = &lsaname($area, 'Network', $lsid, undef);
		$old = $lsdb{$name};
		unless (defined $old && $old->{$Age} < $lsa->{$Age})
		{
		    $lsdb{$name} = $lsa;
		    $netdb{$name} = $lsa; # �ü����Ͽ�򤢤ȤǾä�����
		}
	    }
	    next;
	}

	# Router-LSA Option
	if (/^\s+\#links\s+\d+\s+Option\s+<([^<>]*)>/o)
	{
	    ($opt) = ($1);
	    # $lsa �Ϸ�³����
	    $lsa->{$Text} .= $_;
	    $lsa->{$RtrOpt} = $opt;
	    $lsa->{$Link} = ();

	    $lsa->{$Route} = &rtadd('Router', $lsid, undef, $lsa);
	    if (index($opt, 'E') >= $[)
	    {
		$lsa->{$ASBR} = &rtadd('ASBR', $lsid, undef, $lsa);
	    }
	    next;
	}
	# Router-LSA Link
	if (/^\s+(Point-to-Point|P-to-P|Transit|Stub|Virtual|Vlink)\s+Id\s+(\d+\.\d+\.\d+\.\d+)\s+\s+Data\s+(\d+\.\d+\.\d+\.\d+)\s+Metric\s+(\d+)/o)
	{
	    # $lsa �Ϸ�³����
	    # $link �Ͽ�������
	    ($type, $linkid, $data, $metric) = ($1, $2, $3, $4);
	    $link = {};

	    $link->{$Text} = $_;
	    $link->{$Metric} = int($metric);
	    $link->{$Area} = $area;
	    $link->{$AreaVal} = $areaval;

	    if ($type eq 'Stub')
	    {
		$link->{$LSType} = 'Stub';
		$link->{$LSId} = $linkid;
		$link->{$Mask} = $data;
		$link->{$Stub} = &rtadd('Stub', $linkid, $data, $lsa);
		$link->{$MyAddr} = "self";
	    }
	    elsif ($type eq 'Transit')
	    {
		$link->{$LSType} = 'Network';
		$link->{$LSId} = $linkid;
		push(@linkdb, $link); # ���Ȥ� $link->{$AdvRtr} �����
		$link->{$MyAddr} = "Addr $data";
	    }
	    else
	    {
		$link->{$LSType} = 'Router';
		$link->{$LSId} = $linkid;
		$link->{$AdvRtr} = $linkid;
		if ($type eq 'Virtual'  ||  $type eq 'Vlink')
		{
		    $link->{$MyAddr} = "Virtual $data";
		}
		else
		{
		    $link->{$MyIfp} = "ifIndex $data";
		}
	    }

	    $link->{$LSA} = $lsa;
	    push(@{$lsa->{$Link}}, $link);
	    next;
	}
	
	# Network LSA netmask
	# Summary LSA netmask
	# External LSA netmask
	# NSSA LSA netmask
	if (/^\s+Network Mask (\d+\.\d+\.\d+\.\d+)/o)
	{
	    ($mask) = ($1);
	    $lsa->{$Text} .= $_;
	    if ($lstype eq 'SumRtr')
	    {
		$lsa->{$Route} = &rtadd('ASBR', $lsid, undef, $lsa);
		next;
	    }
	    $lsa->{$Mask} = $mask;
	    $lsa->{$Route} = &rtadd($lstype, $lsid, $mask, $lsa);
	    next;
	}

	# Network LSA link
	if (/^\s+Attached Router\s+(\d+\.\d+\.\d+\.\d+)/o)
	{
	    ($id) = ($1);
	    $link = {};

	    $link->{$Text} = $_;
	    $link->{$Metric} = 0;
	    $link->{$Area} = $area;
	    $link->{$AreaVal} = $areaval;

	    $link->{$LSType} = 'Router';
	    $link->{$LSId} = $id;
	    $link->{$AdvRtr} = $id;
	    $link->{$LSA} = $lsa;
	    $lsa->{$Link} = () unless $lsa->{$Link};
	    push(@{$lsa->{$Link}}, $link);
	    next;
	}

	# Summary LSA
	if (/^\s+TOS\s(\d+)\s+Metric\s+(\d+)/o)
	{
	    ($tos, $metric) = ($1, $2);

	    $lsa->{$Text} .= $_;
	    if (int($tos) == 0)
	    {
		$lsa->{$Metric} = int($metric);
		$origin = $lsdb{&lsaname($area, 'Router', $adv, $adv)};
		if ($origin)
		{
		    push(@{$origin->{$More}}, $lsa);
		    $lsa->{$Back}[$[] = $origin;
		}
	    }
	    next;
	}

	# External LSA
	# NSSA LSA
	if (/^\s+Option\s+<([^<>]*)>\s+TOS\s+(\d+)\s+Metric\s+(\d+)\s+Forwarder\s+(\d+\.\d+\.\d+\.\d+)\s+Tag\s+(\d+)/o)
	{
	    ($opt, $tos, $metric, $forwarder) = ($1, $2, $3, $4);
	    $lsa->{$Text} .= $_;
	    if (int($tos) == 0)
	    {
		$opt = "Type2";
		$lsa->{$ExtOpt} = $opt;
		$lsa->{$Route}->{$ExtOpt} = $opt;
		$lsa->{$Metric} = int($metric);
		$asbrdb{$adv} = () unless $asbrdb{$adv};
		push(@{$asbrdb{$adv}}, $lsa); # ASEͭ����ǧ��
		if ($forwarder ne '0.0.0.0')
		{
		    $lsa->{$Forward} = $forwarder;
		    $forwdb{$forwarder} = 1;
		}
	    }
	    next;
	}
    }
}

sub rtadd
{
    my ($type, $dest, $mask, $lsa) = @_;
    my ($rt, $i);
    $rt = {};
    if ($mask)
    {
	if (defined $masklen{$mask})
	{
	    $dest = &addrmask($dest, $mask);
	}
    }
    else
    {
	$mask = $lsa->{$Area};
    }
    $addr = &rtdest($type, $dest, $mask);
    $rt->{$Addr} = $addr;
    $rt->{$Name} = &rtname($type, $dest, $mask, $lsa);
    $rt->{$Pri} = $rtpri{$type};
    $rt->{$LSA} = $lsa;
    $rt->{$ExtPref} =
	(!$rfc1583compat
	 && $lsa->{$Area} ne '0.0.0.0'
	 && ($lsa->{$LSType} eq 'Router'
	     || $lsa->{$LSType} eq 'Network'))
	? '����' : '����';
    $rt->{$Back} = ();
    $rt->{$More} = ();
    $rtbl{$addr} = () unless $rtbl{$addr};
    push(@{$rtbl{$addr}}, $rt);
    $rt;
}
sub addrmask
{
    my ($addr, $mask) = @_;
    my (@addr, @mask, $i);
    @addr = split(/\./, $addr);
    @mask = split(/\./, $mask);
    for ($i = $[;  $i <= $#mask;  ++$i)
    {
	$addr[$i] = int($addr[$i]) & int($mask[$i])
    }
    for ($i = $#mask + 1;  $i <= $#addr;  ++$i)
    {
	$addr[$i] = 0;
    }
    join('.', @addr);
}
sub setvalid
{
    my ($list) = @_;

    # check primary route
    @pri = ();
    @transSum = ();
    for $rt (@{$list})
    {
	undef $rt->{$Valid};
	next unless defined $rt->{$Cost};
	next if defined $rt->{$Invalid};
	if ($rt->{$MaybeTransit})
	{
	    push(@transSum, $rt);
	    next;
	}
	if (@pri)
	{
	    if ($pri[$[]->{$Pri} < $rt->{$Pri})
	    {
		next;
	    }
	    if ($pri[$[]->{$Pri} > $rt->{$Pri})
	    {
		@pri = ($rt);
		next;
	    }
	    if ($rt->{$Pri} == $rtpri{'External'})
	    {
		if (!$pri[$[]->{$ExtOpt} &&  $rt->{$ExtOpt})
		{
		    next;
		}
		if ( $pri[$[]->{$ExtOpt} && !$rt->{$ExtOpt})
		{
		    @pri = ($rt);
		    next;
		}
		if ($rt->{$ExtOpt})
		{
		    if ($pri[$[]->{$Cost} < $rt->{$Cost})
		    {
			next;
		    }
		    if ($pri[$[]->{$Cost} > $rt->{$Cost})
		    {
			@pri = ($rt);
			next;
		    }
		}
		if ($extpref{$pri[$[]->{$Back}[$[]->{$ExtPref}} < $extpref{$rt->{$Back}[$[]->{$ExtPref}})
		{
		    next;
		}
		if ($extpref{$pri[$[]->{$Back}[$[]->{$ExtPref}} < $extpref{$rt->{$Back}[$[]->{$ExtPref}})
		{
		    @pri = ($rt);
		    next;
		}
	    }
	    elsif ($rt->{$Pri} == $rtpri{'ASBR'})
	    {
		if ($extpref{$pri[$[]->{$ExtPref}} < $extpref{$rt->{$ExtPref}})
		{
		    next;
		}
		if ($extpref{$pri[$[]->{$ExtPref}} > $extpref{$rt->{$ExtPref}})
		{
		    @pri = ($rt);
		    next;
		}
	    }
	    if ($pri[$[]->{$Cost} < $rt->{$Cost})
	    {
		next;
	    }
	    if ($pri[$[]->{$Cost} > $rt->{$Cost})
	    {
		@pri = ($rt);
		next;
	    }
	    if ($rt->{$ExtOpt})
	    {
		if ($pri[$[]->{$Type1Cost} < $rt->{$Type1Cost})
		{
		    next;
		}
		if ($pri[$[]->{$Type1Cost} > $rt->{$Type1Cost})
		{
		    @pri = ($rt);
		    next;
		}
	    }
	}
	push(@pri, $rt);
    }
    if (@pri)
    {
	for $rt (@transSum)
	{
	    if ($rt->{$Cost} > $pri[$[]->{$Cost})
	    {
		next;
	    }
	    if ($rt->{$Cost} < $pri[$[]->{$Cost})
	    {
		@pri = ();
	    }
	    push(@pri, $rt);
	}
    }
    for $rt (@pri)
    {
	$rt->{$Valid} = 1;
    }
}
sub getvalid
{
    my ($addr) = @_;
    &getvalidfromlist($rtbl{$addr});
}
sub getvalidfromlist
{
    my ($list) = @_;
    my ($rt);

    for $rt (@{$list})
    {
	return $rt if $rt->{$Valid};
    }
    undef;
}

################
# ������ɤ߽�������
# Router-LSA ���� Transit Link ��Ŭ���ˤ���
# Network-LSA �� lsdb �ؤ��ü����Ͽ�򳰤�
################
for $link (@linkdb)
{
    $net = $lsdb{&lsaname($link->{$Area}, 'Network',
			  $link->{$LSId}, undef)};
    if ($net)
    {
	$link->{$AdvRtr} = $net->{$AdvRtr};
    }
}
for $name (keys %netdb)
{
    undef $lsdb{$name};
}

################################################################
# ��ϩ�׻�
################################################################
# ���ꥢ��
################
@cand = ();
%lsapri = ('Network' => 1,
	   'Router' => 2,
	   'Stub' => 3,
	   'SumRtr' => 4,
	   'SumNet' => 5,
	   'External' => 6,
	   'NSSA' => 6);
sub pushlink
{
    my ($link) = @_;
    my ($cost, $areaval) = ($link->{$Cost}, $link->{$AreaVal});
    my ($pri, $i);
    $pri = $lsapri{$link->{$LSType}};
    $link->{$Pri} = $pri;
    for ($i = $[;  $i <= $#cand;  ++$i)
    {
	next if $cand[$i]->{$Cost} < $cost;
	last if $cand[$i]->{$Cost} > $cost;
	next if $cand[$i]->{$Pri} < $pri;
	last if $cand[$i]->{$Pri} > $pri;
	next if $cand[$i]->{$AreaVal} < $areaval;
	last if $cand[$i]->{$AreaVal} > $areaval;
    }
    splice(@cand, $i, 0, $link);
}

while (($area, $val) = each %area)
{
    next if $area eq 'Global';
    $link = {};
    $link->{$Area} = $area;
    $link->{$AreaVal} = &addrval($area);
    $link->{$LSType} = 'Router';
    $link->{$LSId} = $self;
    $link->{$AdvRtr} = $self;
    $link->{$Cost} = $SelfCost;
    # �� �����ʤ� {$Cost} = 0 �Ȥ��٤��ս������
    # FALSE Ƚ�ꤵ��Ƥ��ޤ��Τ�����������㲽��
    $link->{$Root} = 1;
    pushlink($link);
}
@root = @cand;

# @cand ����ҤȤĤŤĥ����å�
while (@cand)
{
    $link = shift(@cand);

    $lsa = $lsdb{&lsaname($link->{$Area}, $link->{$LSType},
			  $link->{$LSId}, $link->{$AdvRtr})};
    # link �� LSA ��¸�ߤ� Age �γ�ǧ
    next unless $lsa;
    if (!defined($lsa->{$Age})  ||  $lsa->{$Age} >= 3600)
    {
	$link->{$Invalid} = 'MaxAge';
	$lsa->{$Invalid} = 'MaxAge';
	next;
    }

    # Root ����ʤ� LSA ������С���ϩ�׻��оݥ��ꥢ�Ȥ�����Ͽ����
    # ���Ȥǥ��ޥ�׻����뤫�ɤ�����Ƚ�Ǥ˻Ȥ���
    $parent = $link->{$LSA};
    $area = $link->{$Area};
    if ($parent)
    {
	$validarea{$area} = 1;
    }

    # �����ȳ�ǧ
    next if (defined($lsa->{$Cost}) && $lsa->{$Cost} < $link->{$Cost});

    $rt = $lsa->{$Route};
    $asbr = $lsa->{$ASBR};

    # LinkBack ��ǧ�� Peer addr ����
    if ($parent)
    {
	$lstype = $parent->{$LSType};
	$lsid = $parent->{$LSId};
	$rtr = $parent->{$AdvRtr};
	for $back (@{$lsa->{$Link}})
	{
	    if ($back->{$LSType} eq $lstype
		&& $back->{$LSId} eq $lsid
		&& $back->{$AdvRtr} eq $rtr)
	    {
		$link->{$LinkBackOk} = 1;
		$back->{$BackLink} = 1;
		push(@{$parent->{$More}}, $lsa);
		push(@{$parent->{$Route}->{$More}}, $rt);
		push(@{$parent->{$Route}->{$More}}, $asbr) if $asbr;
		push(@{$lsa->{$Back}}, $parent);
		push(@{$rt->{$Back}}, $parent->{$Route});
		push(@{$asbr->{$Back}}, $parent->{$Route}) if $asbr;
		$peer = $back->{$MyAddr} || $link->{$MyIfp};
		last;
	    }
	}
	unless ($link->{$LinkBackOk})
	{
	    $link->{$Invalid} = 'NoBackLink';
	    next;
	}
    }

    # OK.
    if (defined($lsa->{$Cost}) && $lsa->{$Cost} > $link->{$Cost})
    {
	# reset gateway
	$lsa->{$Gateway} = {};
	$rt->{$Gateway} = {} if $rt;
	$asbr->{$Gateway} = {} if $asbr;
    }
    if ($lsa->{$LSType} eq 'Router'
	&& $area ne '0.0.0.0'
	&& index($lsa->{$RtrOpt}, 'V') >= $[)
    {
	$transit{$area} = 1;
    }
    $lsa->{$Cost} = $link->{$Cost};
    $rt->{$Cost} = $lsa->{$Cost} if $rt;
    $asbr->{$Cost} = $lsa->{$Cost} if $asbr;

    # $self �⤷���� $self ���� Network �ˤ� {$Root} ����
    # �ʱ�ˤ� {$Gateway} ����
    if ($link->{$Root})
    {
	if ($lsa->{$LSType} eq 'Network')
	{
	    $gw = 'Connected';
	    $lsa->{$Gateway}->{$gw} = $parent->{$Name};
	    $rt->{$Gateway} = $lsa->{$Gateway} if $rt;
	}
	for $next (@{$lsa->{$Link}})
	{
	    if ($next->{$LSType} eq 'Network')
	    {
		$next->{$Root} = 1;
	    }
	    else
	    {
		$next->{$Peer} = 1;
	    }
	}
    }
    else
    {
	if ($link->{$Peer})
	{
	    $lsa->{$Gateway}->{$peer} = $lsa->{$Name};
	}
	while (($gw, $val) = each %{$parent->{$Gateway}})
	{
	    next if $gw eq 'Connected';
	    $lsa->{$Gateway}->{$gw} = $val;
	}
	$rt->{$Gateway} = $lsa->{$Gateway} if $rt;
	$asbr->{$Gateway} = $lsa->{$Gateway} if $asbr;
    }

    # Link ��Ͽ
    for $next (@{$lsa->{$Link}})
    {
	$next->{$Cost} = $lsa->{$Cost} + $next->{$Metric};
	if ($next->{$LSType} eq 'Stub')
	{
	    $rt = $next->{$Stub};
	    $rt->{$Cost} = $next->{$Cost} if $rt;
	    next;
	}
	&pushlink($next);
    }

    push(@tree, $lsa);
}

################
# ���ޥ�
################
$bb = $validarea{'0.0.0.0'};
for $rtr (@tree)
{
    next unless $rtr->{$LSType} eq 'Router';
    for $sum (@{$rtr->{$More}})
    {
	next unless ($sum->{$LSType} eq 'SumNet'
		     || $sum->{$LSType} eq 'SumRtr');
	$rt = $sum->{$Route};
	if ($rtr->{$Cost} <= 0)
	{
	    $sum->{$Invalid} = '��ʬ�����ʥ��󥹤��Ƥ��ۤʤΤ�̵��';
	    $rt->{$Invalid} = '��ʬ�����ʥ��󥹤��Ƥ��ۤʤΤ�̵��';
	    next;
	}
	if (!defined($sum->{$Age}) || $sum->{$Age} >= 3600)
	{
	    $sum->{$Invalid} = 'MaxAge';
	    $rt->{$Invalid} = 'MaxAge';
	    next;
	}
	if (!defined($sum->{$Metric}) || $sum->{$Metric} >= 0xffffff)
	{
	    $sum->{$Invalid} = '������ ��';
	    $rt->{$Invalid} = '������ ��';
	    next;
	}
	if ($bb  &&  $rtr->{$Area} ne '0.0.0.0')
	{
	    if ($transit{$rtr->{$Area}})
	    {
		$cost = $rtr->{$Cost} + $sum->{$Metric};
		$sum->{$Cost} = $cost;
		$rt->{$Cost} = $cost;
		$gw = $rtr->{$Gateway};
		$sum->{$Gateway} = $gw;
		$rt->{$Gateway} = $gw;
		$rt->{$MaybeTransit} = 1;
		push(@tree, $sum);
	    }
	    else
	    {
		$sum->{$Invalid} ='�Хå��ܡ��󥨥ꥢ�ǤϤʤ��Τ�̵��';
		$rt->{$Invalid} = '�Хå��ܡ��󥨥ꥢ�ǤϤʤ��Τ�̵��';
	    }
	}
	else
	{
	    $cost = $rtr->{$Cost} + $sum->{$Metric};
	    $sum->{$Cost} = $cost;
	    $rt->{$Cost} = $cost;
	    $gw = $rtr->{$Gateway};
	    $sum->{$Gateway} = $gw;
	    $rt->{$Gateway} = $gw;
	    $rt->{$Back}[$[] = $rtr;
	    push(@tree, $sum);
	}
    }
}

################
# ���Ƥ��Τؤ�ǰ��١����ꥢ���ϩ�ȥ��ޥ��ϩ��ͥ���٤��������Ƥ�����
################
while (($addr, $list) = each %rtbl)
{
    &setvalid($list);
}

################
# �Ǹ�� ASE �� NSSA
################
# ������ Forwarder ���Ф��� NET ��ϩ��ҤäѤäư����ˤ��Ƥ���
# ���λ����ǤϤޤ� External �� NSSA �� {'Valid '} ���դ��Ƥʤ��Τ�
# ���ꥢ��ޤ��ϥ��ꥢ�֥ѥ��Τߤ�ȤäƳ�ǧ�Ǥ���
@forwarder = keys %forwdb;
%forwdb = ();
for $forwarder (@forwarder)
{
    for ($i = $#masklen;  $i >= 0;  --$i)
    {
	$rt = &getvalid(&rtdest('Network', &addrmask($forwarder, $masklen[$i]), $masklen[$i]));
	next unless $rt;
	$forwdb{$forwarder} = $rt;
    }
}

# ASBR ���˳�����ϩ���ǧ������ǽ�ʤ� {$Valid} ��Ω�Ƥ�
# �⤷ Forwarder �⤢��С��Ĥ������������ۤ��� %forwdb ��Ȥ�
while (($adv, $aselist) = each %asbrdb)
{
    $asbr = &getvalid(&rtdest('ASBR', $adv, undef));
    next unless $asbr;
    if ($asbr->{$Invalid})
    {
	for $ase (@{$aselist})
	{
	    push(@{$asbr->{$More}}, $ase);
	    $ase->{$Invalid} = $rt->{$Invalid};
	}
	next;
    }
    if ($asbr->{$Cost} eq $SelfCost)
    {
	for $ase (@{$aselist})
	{
	    push(@{$asbr->{$More}}, $ase);
	    $ase->{$Invalid} = '��ʬ�����ʥ��󥹤��Ƥ��ۤʤΤ�̵��';
	    $ase->{$Route}->{$Invalid} = '��ʬ�����ʥ��󥹤��Ƥ��ۤʤΤ�̵��';
	}
	next;
    }
    for $ase (@{$aselist})
    {
	push(@{$asbr->{$More}}, $ase);
	$rt = $ase->{$Route};
	if (!defined($ase->{$Age})  ||  $ase->{$Age} >= 3600)
	{
	    $ase->{$Invalid} = 'MaxAge';
	    $rt->{$Invalid} = 'MaxAge';
	    next;
	}
	if (!defined($ase->{$Metric})  ||  $ase->{$Metric} >= 0xffffff)
	{
	    $ase->{$Invalid} = '������ ��';
	    $rt->{$Invalid} = '������ ��';
	    next;
	}
	if ($ase->{$Forward})
	{
	    $forw = $forwdb{$ase->{$Forward}};
	    next unless $forw;
	    push(@{$forw->{$More}}, $ase);
	    $rt->{$Forward} = $ase->{$Forward};
	    $ase->{$Back}[$[] = $forw;
	    $rt->{$Back}[$[] = $forw;
	    if ($ase->{$ExtOpt})
	    {
		$cost1 = $ase->{$Metric};
		$ase->{$Cost} = $cost1;
		$rt->{$Cost} = $cost1;
		$gw = $forw->{$Gateway};
		$ase->{$Gateway} = $gw;
		$rt->{$Gateway} = $gw;
		$cost2 = $forw->{$Cost};
		$cost = $cost1 + $cost2;
		$ase->{$Type1Cost} = $cost;
		$rt->{$Type1Cost} = $cost;
	    }
	    else
	    {
		$cost1 = $ase->{$Metric};
		$cost2 = $forw->{$Cost};
		$cost = $cost1 + $cost2;
		$ase->{$Cost} = $cost;
		$rt->{$Cost} = $cost;
		$gw = $forw->{$Gateway};
		$ase->{$Gateway} = $gw;
		$rt->{$Gateway} = $gw;
	    }
	}
	else
	{
	    $ase->{$Back}[$[] = $asbr;
	    $rt->{$Back}[$[] = $asbr;
	    if ($ase->{$ExtOpt})
	    {
		$cost1 = $ase->{$Metric};
		$ase->{$Cost} = $cost1;
		$rt->{$Cost} = $cost1;
		$cost2 = $asbr->{$Cost};
		$cost = $cost1 + $cost2;
		$ase->{$Type1Cost} = $cost;
		$rt->{$Type1Cost} = $cost;
		$gw = $asbr->{$Gateway};
		$ase->{$Gateway} = $gw;
		$rt->{$Gateway} = $gw;
	    }
	    else
	    {
		$cost1 = $ase->{$Metric};
		$cost2 = $asbr->{$Cost};
		$cost = $cost1 + $cost2;
		$ase->{$Cost} = $cost;
		$rt->{$Cost} = $cost;
		$gw = $asbr->{$Gateway};
		$ase->{$Gateway} = $gw;
		$rt->{$Gateway} = $gw;
	    }
	}
	push(@tree, $ase);
	$asedb{$rt->{$Addr}} = 1; # �ɲä����ä����ɥ쥹��Ф��Ȥ�
    }
}
# �ɲä����ä����ɥ쥹�κ�ͥ���ϩ����ľ��
while (($addr, $val) = each %asedb)
{
    &setvalid($rtbl{$addr});
}

# %rtbl �����˥����Ȥ���
%rttype = ('�ͥåȥ�����ɥ쥹' => 1, 'AS�����롼��' => 2, '�롼��ID' => 3);
while (($dest, $list) = each %rtbl)
{
    @dest = split(/[:\.]/, $dest);
    $dest[$[] = $rttype{$dest[$[]};
    $rtval{$dest} = ();
    push(@{$rtval{$dest}}, @dest);
}
sub sortaddr
{
    my ($i, $aa, $bb, $len, $lencmp);
    $aa = $rtval{$a};
    $bb = $rtval{$b};
    $lencmp = $#{$aa} - $#{$bb};
    $len = $#{$aa};
    $len = $#{$bb} if $#{$bb} < $len;
    for ($i = $[;  $i <= $len;  ++$i)
    {
	return ${$aa}[$i] <=> ${$bb}[$i] if ${$aa}[$i] != ${$bb}[$i];
    }
    $lencmp;
}
@rtaddrs = sort sortaddr keys %rtbl;

# �Ǹ�ˡ���ã�Բ�ǽ���ä�������ꥹ�Ȥ˼�����
for ($i = $[;  $i <= $#tree;  ++$i)
{
    $tree[$i]->{$OnTree} = 1;
}
while (($name, $lsa) = each %lsdb)
{
    next unless $lsa;
    if ($lsa->{$OnTree})
    {
	undef $lsa->{$OnTree};
	next;
    }
    push(@tree, $lsa);
    next if $lsa->{$Invalid};
    &setunreach($lsa);
    &setunreach($lsa->{$Route});
    &setunreach($lsa->{$ASBR});
    for $link (@{$lsa->{$Link}})
    {
	&setunreach($link->{$Stub});
    }
}
sub setunreach
{
    my ($item) = @_;
    $item->{$Invalid} = 'Unreachable' if $item;
}

################################################################
# �������Ƥ��ɤ߹�������Ƥʤɤ�١�����
# �ǡ������ϥե������ɽ������
################################################################
print $q->start_multipart_form."\n";
print $q->ul($q->li($q->filefield('db'), 'show ip ospf database detail �ˤ�äƼ��������ե�����'),
	     $q->param('db') ? $q->ul($q->li($q->param('db'))) : undef,
	     $q->li($q->textfield('routerid', $self),
		    '��ϩ�׻��������롼���� Router ID (show ip ospf database detail �˴ޤޤ�Ƥ��������) '),
	     $self ? $q->ul($q->li("Router ID = $self")) : undef,
	     $q->li($q->checkbox(-name => 'RFC1583Compat',
				 -checked => $q->param('RFC1583Compat'),
				 -value => 'on')),
	     $q->li($q->checkbox(-name => 'debug',
				 -value => 'on')));
print $q->submit('calc', '�׻�')
    . $q->reset
    . $q->submit('description', '���Υץ����������ȻȤ�����')
    . $q->submit('source', '���Υץ����Υ�����������')
    . $q->submit('history', '��ȯ����')
    . $q->submit('todo', 'ToDo')
    . $q->submit('thanksto', 'Thanks To')
    . "\n";

if ($q->param('description'))
{
    &description;
    print $q->end_div;
    print $q->end_html;
    exit 0;
}

if ($q->param('history'))
{
    &show_and_exit('��������', @history);
    exit 0;
}
if ($q->param('todo'))
{
    &show_and_exit('ToDo', @todo);
    exit 0;
}
if ($q->param('thanksto'))
{
    &show_and_exit('Thanks to', @thanksto);
    exit 0;
}

if (!$q->param('db'))
{
    print $q->end_form . "\n";
    print $q->end_div;
    print $q->end_html;
    exit;
}

print $q->br . 'Jump to ';
print $q->a({-href => '#%rtbl'}, "��ϩɽ");
print $q->br . 'Jump to ';
print $q->a({-href => '#%lsdb'}, "LSDB") . "\n";


################################################################
# show ip ospf route
################################################################
print $q->hr;
print $q->a({-name => '%rtbl'}, "��ϩɽ") . $q->br . "\n";
%ignore = ($Name => 1,
	   $Pri => 1,
	   $Addr => 1) unless $debug;
$ignore{$ExtOpt} = 1 if !$debug && $rfc1583compat;
for $addr (@rtaddrs)
{
    $list = $rtbl{$addr};
    $txt1 = &getvalid($addr) ? "*" : " ";
    $txt1 .= " $addr";
    print $q->a({-name => $addr}, $txt1)."\n";
    for $rt (@{$list})
    {
	$txt1 = $rt->{$Valid} ? "* " : "  ";
	$txt1 .= $lsadesc{$rt->{$LSA}->{$LSType}} . ' ';
	$txt1 .= $q->a({-name => $rt->{$Name}}, $rt->{$Addr})."\n";

	$txt2 = '';
	while (($tag, $val) = each %{$rt})
	{
	    next unless $val;
	    next if $ignore{$tag};
	    if ($tag eq $More  ||  $tag eq $Back)
	    {
		# ARRAYs (#href #val)
		for $more (@{$val})
		{
		    $txt3 = $more->{$Name};
		    $txt4 = $more->{$Addr} || $txt3;
		    $txt3 = $q->a({-href => "#$txt3"}, $txt4);
		    $txt2 .= "\t[$tag = $txt3]\n";
		}
		next;
	    }
	    if ($tag eq $Gateway)
	    {
		# HASH keys (href #val)
		while (($txt3, $val3) = each %{$val})
		{
		    $txt3 = $q->a({-href => "#$val3"}, $txt3);
		    $txt2 .= "\t[$tag = $txt3]\n";
		}
		next;
	    }
	    if ($tag eq $LSA)
	    {
		# Links
		$txt3 = $val->{$Name};
		$txt3 = $q->a({-href => "#$txt3"}, $txt3);
		$txt2 .=  "\t[$tag = $txt3]\n";
		next;
	    }
	    $txt2 .= "\t[$tag = $val]\n";
	}
	$txt1 .= $q->i($txt2);
	$txt1 = $q->pre($txt1);
	$txt1 = $q->blockquote({-style => 'border: 3px double;'}, $txt1);
	print "$txt1\n";
    }
}

################################################################
# show ip ospf database
################################################################
print $q->hr;
print $q->a({-name => '%lsdb'}, "LSDB") . $q->br . "\n";
%ignore = ($Name => 1,
	   $Text => 1,
	   $LSId => 1,
	   $Mask => 1,
	   $Area => 1,
	   $AreaVal => 1,
	   $LSType => 1,
	   $LSId => 1,
	   $AdvRtr => 1,
	   $Age => 1,
	   $Opt => 1,
	   $RtrOpt => 1,
	   $Pri => 1,
	   $Metric => 1,
	   $Link => 1,
	   $MyAddr => 1,
	   $MyIfp => 1,
	   $Root => 1,
	   $Peer => 1,
	   $ExtOpt => 1,
	   $OnTree => 1) unless $debug;
for $lsa (@tree)
{
    $txt1 = "Area " . $lsa->{$Area};
    $txt1 .= ",  Cost " . $lsa->{$Cost} if defined $lsa->{$Cost};
    print "$txt1\n";

    $txt1 = $q->escapeHTML($lsa->{$Text});
    $txt1 = $q->a({-name => $lsa->{$Name}}, $txt1) . "\n";

    $txt2 = '';
    while (($tag, $val) = each %{$lsa})
    {
	next unless $val;
	next if $ignore{$tag};
	if ($tag eq $More  ||  $tag eq $Back)
	{
	    # ARRAYs
	    for $more (@{$val})
	    {
		$txt3 = $more->{$Name};
		$txt4 = $more->{$Addr} || $txt3;
		$txt3 = $q->a({-href => "#$txt3"}, $txt4);
		$txt2 .= "\t[$tag = $txt3]\n";
	    }
	    next;
	}
	if ($tag eq $Gateway)
	{
	    # HASH keys (href #val)
	    while (($txt3, $val3) = each %{$val})
	    {
		$txt3 = $q->a({-href => "#$val3"}, $txt3);
		$txt2 .= "\t[$tag = $txt3]\n";
	    }
	    next;
	}
	if ($tag eq $Route  ||  $tag eq $ASBR)
	{
	    $txt3 = $val->{$Name};
	    $txt4 = $val->{$Addr} || $txt3;
	    $txt3 = $q->a({-href => "#$txt3"}, $txt4);
	    $txt2 .= "\t[$tag = $txt3]\n";
	    next;
	}
	$txt3 = "\t[$tag = $val]\n";
	$txt2 .= $txt3;
    }
    $txt1 .= $q->i($txt2);

    for $link (@{$lsa->{$Link}})
    {
	$txt2 = $link->{$Text};
	if ($txt2 =~ /^\s*(\S.+)\s*$/o)
	{
	    $txt3 = $1;
	    $ref = &lsaname($lsa->{$Area}, $link->{$LSType},
			    $link->{$LSId}, $link->{$AdvRtr});
	    $txt3 = $q->a({-href => "#$ref"}, $txt3);
	    $txt2 =~ s/^(\s*)\S.*(\s*)$/$1$txt3$2/g;
	}
	$txt1 .= "\n$txt2";

	$txt2 = "";
	while (($tag, $val) = each %{$link})
	{
	    next unless $val;
	    next if $ignore{$tag};
	    if ($tag eq $Gateway)
	    {
		# HASH keys (href #val)
		while (($txt3, $val3) = each %{$val})
		{
		    $txt3 = $q->a({-href => "#$val3"}, $txt3);
		    $txt2 .= "\t[$tag = $txt3]\n";
		}
		next;
	    }
	    if ($tag eq $LSA || $tag eq $Stub)
	    {
		$txt3 = $val->{$Name};
		$txt4 = $val->{$Addr} || $txt3;
		$txt3 = $q->a({-href => "#$txt3"}, $txt4);
		$txt2 .= "\t\t[$tag = $txt3]\n";
		next;
	    }
	    $txt2 .= "\t\t[$tag = $val]\n";
	}
	$txt1 .= $q->i($txt2);
    }
    $txt1 = $q->pre($txt1);
    $txt1 = $q->blockquote({-style => 'border: 3px double;'}, $txt1)."\n";
    $txt1 .= $q->br;
    print "$txt1\n";
}

################################################################
# ʸ��
################################################################
print '(�ʲ�;��)' . $q->br x 100;
print $q->end_div;
print $q->end_html;
