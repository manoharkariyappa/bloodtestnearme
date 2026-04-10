frappe.pages['offline-dashboard'].on_page_load = function(wrapper) {

	let page = frappe.ui.make_app_page({
		parent: wrapper,
		title: 'Offline Orders',
		single_column: true
	});

	$(page.body).html(`

	<style>
		.orders-container {
			padding: 20px;
			background: #f5f6f8;
		}

		/* ✅ Tabs + Button */
		.order-tabs {
			margin-bottom: 15px;
			border-bottom: 1px solid #d1d8dd;
			display: flex;
			justify-content: space-between;
			align-items: center;
		}

		.tabs-left {
			display: flex;
			gap: 20px;
		}

		.order-tabs .tab {
			cursor: pointer;
			font-weight: 600;
			padding-bottom: 8px;
			color: #444;
			font-size: 14px;
		}

		.order-tabs .active {
			color: #2490ef;
			border-bottom: 2px solid #2490ef;
		}

		/* ✅ Button Style */
		.create-order-btn {
			background: #2490ef;
			color: white;
			border: none;
			padding: 6px 12px;
			border-radius: 4px;
			cursor: pointer;
			font-weight: 600;
			font-size: 13px;
		}

		.create-order-btn:hover {
			background: #1b7cd6;
		}

		.filters {
			margin-bottom: 15px;
			display: flex;
			gap: 10px;
		}

		.filter-box {
			padding: 6px;
			border: 1px solid #ccc;
			border-radius: 3px;
			min-width: 180px;
		}

		table {
			width: 100%;
			border-collapse: collapse;
			background: white;
		}

		table thead {
			background: #f0f2f5;
		}

		table th, table td {
			padding: 10px;
			text-align: center;
			border-bottom: 1px solid #e4e7eb;
			font-size: 14px;
		}

		table tbody tr:hover {
			background: #f9fbfd;
			cursor: pointer;
		}

		.no-data {
			text-align: center;
			padding: 20px;
			color: #888;
		}
	</style>

	<div class="orders-container">

		<!-- ✅ Tabs + Button -->
		<div class="order-tabs">
			<div class="tabs-left">
				<span class="tab active" data-status="Ordered">NEW ORDERS</span>
				<span class="tab" data-status="Completed">COMPLETED</span>
			</div>

			<button class="create-order-btn"> + Add Offline Order</button>
		</div>

		<div class="filters">
			<input type="text" id="search-box" class="filter-box" placeholder="Search...">
		</div>

		<div class="table-responsive">
			<table id="orders-table">
				<thead>
					<tr>
						<th>Id</th>
						<th>Appointment Date</th>
						<th>Appointment Time</th>
						<th>Customer Name</th>
						<th>Total Price</th>
						<th>Mobile</th>
					</tr>
				</thead>
				<tbody></tbody>
			</table>
		</div>

	</div>
	`);

	// Initial Load
	load_orders("Ordered");

	// TAB CLICK
	$(page.body).on("click", ".tab", function() {
		$(".tab").removeClass("active");
		$(this).addClass("active");

		let status = $(this).data("status");
		load_orders(status);
	});

	// SEARCH
	$(page.body).on("keyup", "#search-box", function() {
		let value = $(this).val().toLowerCase();
		$("#orders-table tbody tr").filter(function() {
			$(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
		});
	});

	// ✅ BUTTON CLICK (ROUTE)
	$(page.body).on("click", ".create-order-btn", function() {
		// Change route if needed
		frappe.set_route('/app/offline-order/new-offline-order');
	});
};


// LOAD ORDERS FUNCTION
function load_orders(status) {

	frappe.call({
		method: "bloodtestnearme.api.order_api.get_offline_orders",
		args: {
			status: status,
		},
		callback: function(r) {

			if (!r.message || r.message.status !== "success") {
				frappe.msgprint("Failed to load orders");
				return;
			}

			let data = r.message.data;
			let rows = "";

			if (!data || data.length === 0) {
				rows = `<tr><td colspan="8" class="no-data">No Orders Found</td></tr>`;
			} else {
				data.forEach(order => {
					rows += `
						<tr onclick="frappe.set_route('Form','Offline Order','${order.name}')">
							<td>${order.name || ""}</td>
							<td>${order.appointment_date || ""}</td>
							<td>${order.appointment_time || ""}</td>
							<td>${order.customer_name || ""}</td>
							<td>${order.total_price || ""}</td>
							<td>${order.mobile_number || ""}</td>
						</tr>
					`;
				});
			}

			$("#orders-table tbody").html(rows);
		}
	});
}