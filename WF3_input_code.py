import logging
import time
from tests.network.mgmt_protocols.snmp.snmp_base import TestWhenWorkingSNMPAccessOption
 
class TestWhenVerifyingSNMPGetSetWalkGetNextForMibOrGroupThenSucceeds(TestWhenWorkingSNMPAccessOption):
    """
    Test SNMP Get, Set, Walk, GetNext operations for various MIBs/groups.
    """
 
    @classmethod
    def setup_class(cls):
        """Initialize shared test resources."""
        super().setup_class()
 
"""$$$$$__BEGIN_TEST_METADATA_DECLARATION__$$$$$
    +testcase_id:C52021619
    +title:Verify SNMP Walk_Get_GetNext operation on officeQualityPdlPqMode
    $$$$$__END_TEST_METADATA_DECLARATION__$$$$$"""
def test_when_verifying_snmp_walk_get_getnext_operation_on_officequalitypdlpqmode_then_returns_expected(self):
        """
        1. Open SNMP command tool or run via pytest.
        2. Walk: Use TEST_OID for snmpwalk.
        3. Get: Use same OID for snmpget.
        4. GetNext: Use OID for snmpgetnext.
        Expected: Walk, Get, GetNext should succeed.
        """
        oid_name = "officeQualityPdlPqMode"
        config = self.retrieve_snmp_data_via_oid_name(oid_name)
        test_oid = config["oid"]
        data_type = self.convert_data_type(config["data_type"])
        next_oid = config["next_oid"]
        logging.info(f"Test OID: {test_oid} for {oid_name}, Data Type: {data_type}, Next OID: {next_oid}")
 
        # Walk
        oid_value = self.snmp_client.walk(test_oid)
        assert isinstance(oid_value, list), f"Walk operation did not return a list: {oid_value}"
        logging.info(f"Walk operation on OID-{test_oid} returned: {oid_value}")
 
        # Get
        value = self.snmp_client.get(test_oid, data_type)
        logging.info(f"Get operation on OID-{test_oid} returned: {value}")
 
        # GetNext
        actual_next_oid = self.snmp_client.get_next(test_oid)[0]
        logging.info(f"GetNext actual next OID: {actual_next_oid}")
        assert actual_next_oid == next_oid, f"GetNext operation on OID-{test_oid} returned incorrect next OID: {actual_next_oid}, expected: {next_oid}"