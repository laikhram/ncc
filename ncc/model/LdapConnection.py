import ldap

from model.User import User


class LdapConnection() :

    @staticmethod
    def getLdapConnection(username, password):
        ldap_server = "ldap://ldap.kmutt.ac.th"
        # username = "56130500059"
        # password = "kmutt_IT19"
        # the following is the user_dn format provided by the ldap server
        user_dn = "uid=" + username + ",ou=People,ou=st,dc=kmutt,dc=ac,dc=th"
        # adjust this to your base dn for searching
        base_dn = "dc=kmutt,dc=ac,dc=th"
        connect = ldap.initialize(ldap_server)
        search_filter = "uid=" + username
        try:
            # if authentication successful, get the full user data
            connect.bind_s(user_dn, password)
            result = connect.search_s(base_dn, ldap.SCOPE_SUBTREE, search_filter)
            # return all user data results
            connect.unbind_s()
            # print result
            result = LdapConnection.orm(result)
        except ldap.LDAPError as ex:
            connect.unbind_s()
            print "authentication error"
            raise ex
        return result


    @staticmethod
    def orm(ldap):
        ldapDict = ldap[0][1]
        print ldapDict
        user = User(ldapDict['uid'][0], ldapDict['displayName'][0], ldapDict['sn'][0])
        # return ldapDict['uid'][0] + ", " + ldapDict['displayName'][0] + ", " +ldapDict['sn'][0]
        return user