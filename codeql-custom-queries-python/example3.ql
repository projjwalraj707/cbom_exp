import python
import semmle.python.dataflow.new.DataFlow
import semmle.python.dataflow.new.TaintTracking
import semmle.python.ApiGraphs

module MyFlow implements DataFlow::ConfigSig {
	predicate isSource(DataFlow::Node source) {
		source instanceof DataFlow::ExprNode
	}
	predicate isSink(DataFlow::Node sink) {
		sink = API::moduleImport("Crypto").getMember("PublicKey").getMember("RSA").getMember("generate").getACall()
	}
}

module MyFlow = TaintTracking::Global<MyFlowConfiguration>;